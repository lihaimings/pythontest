from langchain_core.output_parsers import StrOutputParser
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

result = vector_store.similarity_search(input_text,2)
print(result)

reference_txt = "["
for k in result:
    reference_txt+=k.page_content
reference_txt+="]"

def print_prompt(input):
    print("="*20,input)
    return input

chain = prompt |print_prompt | model | StrOutputParser()

res = chain.invoke({"input":input_text,"context":reference_txt})
print(res)