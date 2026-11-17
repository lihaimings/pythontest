from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store = Chroma(
    collection_name="test", #类似表名称
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"
)

# loader = CSVLoader(
#     file_path="./data/info.csv",
#     encoding="utf-8",
#     source_column="source" # 指定本条的数据来源哪里
# )
#
# documents = loader.load()
#
#
# #向量的存储、删除、检索
# vector_store.add_documents(
#     documents = documents,
#     ids=["id"+str(i) for i in range(len(documents))]
# )
#
# #删除
# vector_store.delete(["id1","id2"])

#检索
result = vector_store.similarity_search(
    "python是不是简单易学",
    3,
    filter={"source":"黑马程序员"} #只要黑马程序员的
)

print(result)