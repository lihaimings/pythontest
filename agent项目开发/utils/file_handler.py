import os
import hashlib

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

from utils.logger_handler import logger
def get_file_md_hex(filepath:str):
    if not os.path.exists(filepath):
        logger.error(f"[md5]计算文件{filepath}不存在")
        return
    if not os.path.isfile(filepath):
        logger.error(f"[md5]计算文件{filepath}不是文件")
        return
    md5_obj = hashlib.md5()

    chunk_size = 4096

    try:
        with open(filepath, "rb") as f:
            chunk = f.read(chunk_size)
            while chunk:
                md5_obj.update(chunk)
                chunk = f.read(chunk_size)
            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f"计算文件{filepath}md5实现，{str(e)}")
        return None





def listdir_with_allowed_type(path:str,allowed_type:tuple[str]):
    files = []

    if not os.path.isdir(path):
        logger.error(f"不是文件夹: {path}")
        return files

    for file in os.listdir(path):
        if file.endswith(allowed_type):
            files.append(os.path.join(path,file))

    return files

def pdf_loader(filepath:str,password:str | None = None)->list[Document]:
    return PyPDFLoader(filepath,password).load()

def txt_loader(filepath:str)->list[Document]:
    return TextLoader(filepath,encoding="utf-8").load()
