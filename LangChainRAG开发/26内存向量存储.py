from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    model="qwen3.8-27b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings()
)

loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source" # 指定本条的数据来源哪里
)

documents = loader.load()


#向量的存储、删除、检索
vector_store.add_documents(
    documents = documents,
    ids=["id"+str(i) for i in range(len(documents))]
)

#删除
vector_store.delete(["id1","id2"])

#检索
result = vector_store.similarity_search(
    "python是不是简单易学",
    3
)

print(result)
