from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from vector_stores import VectorStoreService
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import  ChatPromptTemplate,MessagesPlaceholder
from  langchain_openai import ChatOpenAI
from file_history_store import get_histor


def print_prompt(prompt):
    print("=" * 20)
    print(prompt.to_string())
    print("=" * 20)
    return prompt

class RAGService(object):
    def __init__(self):
        self.voctor_service = VectorStoreService(
            embedding= DashScopeEmbeddings()
        )

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system","以我提供的已知参考资料为主,"
                 "简洁和专业的回答用户问题。参考资料：{context}"),
                ("system", "并且我提供用户的对话历史记录如下："),
                MessagesPlaceholder("history"),
                ("user","请回答用户提问：{input}")
            ]
        )
        self.chat_model = ChatOpenAI(
            model="qwen3.8-27b",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",)
        self.chain = self.get_chain()



    def get_chain(self):
        retriever = self.voctor_service.get_retriever()

        def format_document(docs:list[Document]):
            if not docs:
                return "无相关参考资料"
            return "".join(
                f"文档片段:{doc.page_content}\n文档元数据：{doc.metadata}\n\n"
                for doc in docs
            )

        def temp1(value:dict) -> str:
            return value["input"]

        def temp2(value):
            new_value = {}
            new_value["input"] = value["input"]["input"]
            new_value["context"] = value["context"]
            new_value["history"] = value["input"]["history"]
            return new_value

        chain = {
            "input":RunnablePassthrough(),
            "context":RunnableLambda(temp1) | retriever | format_document
        } |RunnableLambda(temp2)| self.prompt_template | print_prompt | self.chat_model | StrOutputParser()

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_histor,
            input_messages_key="input",
            history_messages_key="history"
        )

        return conversation_chain



if __name__ == "__main__":

    res = RAGService().chain.invoke({"input":"怎么洗"},session_config)
    print(res)
