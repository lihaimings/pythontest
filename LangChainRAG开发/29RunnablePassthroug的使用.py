from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from  langchain_openai import ChatOpenAI
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI(
    model="qwen3.8-27b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料：{context}"),
        ("user","用户提问：{input}")
    ]
)

vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings())

vector_store.add_texts(["减肥就是要少吃多练","在减脂期间吃东西很重要，清淡少油减少卡路里摄入并运行起来","跑步是很好的运动哦"])

input_text = "怎么减肥？"

def print_prompt(input):
    print("="*20,input)
    return input

#返回Runnable接口子类实例对象
retriever = vector_store.as_retriever()

def format_func(docs:list[Document]):
    if not docs:
        return "无相关参考资料"
    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
    formatted_str+="]"
    return formatted_str

chain = ({"input":RunnablePassthrough(),"context":retriever | format_func }  | prompt | print_prompt | model | StrOutputParser())


res = chain.invoke(input_text)

print(res)