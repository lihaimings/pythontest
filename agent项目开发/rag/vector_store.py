import os.path
import sys

if not __package__:
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_chroma import Chroma
from langchain_core.documents import Document

from utils.config_handler import chrome_config
from utils.path_tool import get_abs_path
from model.factory import embed_model
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.file_handler import txt_loader,pdf_loader,listdir_with_allowed_type,get_file_md_hex
from utils.logger_handler import logger


class VectorStoreService:


    def __init__(self):
        self.chroma = Chroma(
            collection_name=chrome_config["collect_name"],
            embedding_function=embed_model,
            persist_directory=get_abs_path(chrome_config["persist_directory"]),
        )

        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=chrome_config["chunk_size"],
            chunk_overlap=chrome_config["chunk_overlap"],
            separators=chrome_config["separators"],
            length_function=len
        )

    def get_retriever(self):
        return self.chroma.as_retriever(search_kwargs={"k":chrome_config["k"]})

    def load_document(self):

        def check_md5_hex(md5_for_check:str):
            if not os.path.exists(get_abs_path(chrome_config["md5_hex_store"])):
                open(get_abs_path(chrome_config["md5_hex_store"]), "w",encoding="utf-8").close()
                return False

            with open(get_abs_path(chrome_config["md5_hex_store"]),"r",encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip()
                    if line == md5_for_check:
                        return True

                return False

        def save_md5_hex(md5_for_check:str):
            with open(get_abs_path(chrome_config["md5_hex_store"]),"a",encoding="utf-8") as f:
                f.write(md5_for_check+"\n")

        def get_file_documents(read_path:str):
            if read_path.endswith(".txt"):
                return txt_loader(read_path)
            elif read_path.endswith(".pdf"):
                return pdf_loader(read_path)

        allowed_files_path:list[str] = listdir_with_allowed_type(
            get_abs_path(chrome_config["data_path"]),
            tuple(chrome_config["allow_knowledge_file_type"]),
        )

        for path in allowed_files_path:
            md5_hex = get_file_md_hex(path)

            if check_md5_hex(md5_hex):
                logger.warning(f"已经加载过知识库{md5_hex}")
                continue

            try:
                documents:list[Document] = get_file_documents(path)

                if not documents:
                    logger.warning(f"文件没有内容{path}")
                    continue

                spliter_document :list[Document] = self.spliter.split_documents(documents)

                if not spliter_document:
                    logger.warning("文本分割失败")
                    continue
                self.chroma.add_documents(spliter_document)

                save_md5_hex(md5_hex)

                logger.info(f"加载知识库完成{path}")
            except Exception as e:
                logger.error(f"加载是知识库失败{path},{str(e)}")
                continue



if __name__ == "__main__":
    vs = VectorStoreService()

    vs.load_document()


    retriever = vs.get_retriever()

    res = retriever.invoke("迷路")
    for doc in res:
        print(doc.page_content)
        print("*"*20)
