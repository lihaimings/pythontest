from langchain_chroma import Chroma
import config_data as config
from langchain_community.embeddings import DashScopeEmbeddings


class VectorStoreService(object):
    def __init__(self,embedding):
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )


    def get_retriever(self):
        # k 是返回文档的数量，必须是正整数，不能传入相似度阈值。
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})


if __name__ == "__main__":
    retriever =  VectorStoreService(DashScopeEmbeddings()).get_retriever()

    res = retriever.invoke("我的体重180斤，尺码推荐")

    print(res)
