import os

from sqlalchemy.util import md5_hex

import config_data as config
import hashlib
from langchain_chroma import Chroma
from langchain_community.embeddings import  DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import datetime

def check_md5(md5_str:str):
    """"检查传入的md5是否已经被处理过了"""
    if not os.path.exists(config.md5_path):
        open(config.md5_path,'w',encoding="utf-8").close()
        return False
    for line in open(config.md5_path,'r',encoding="utf-8").readlines():
        line = line.strip()
        if md5_str == line:
            return True
    return False

def save_md5(md5_str:str):
    """"将传入的md5的字符串，记录到文件内保存"""
    with open(config.md5_path,'a',encoding="utf-8") as f:
        f.write(md5_str)

def get_string_md5(input_str:str,encoding="utf-8"):
    """"将传入的字符串转换成md5字符串"""

    # 将字符串转成Bytes数组
    str_bytes = input_str.encode(encoding=encoding)

    # 创建Md5对象
    md5_obj = hashlib.md5()
    md5_obj.update(str_bytes)
    md5_hex = md5_obj.hexdigest()

    return md5_hex

class KnowledgeBaseService(object):

    def __init__(self):
        os.makedirs(config.persist_directory,exist_ok=True)
        self.chroma = Chroma(
            collection_name= config.collection_name, #表名
            embedding_function=DashScopeEmbeddings(),
            persist_directory=config.persist_directory #数据库文件夹
        ) #向量存储的示例chroma向量库对象
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size, #每段的最大数量
            chunk_overlap=config.chunk_overlap, #每段的最大重叠数量
            separators=config.separators, #段落的而划分符号
            length_function=len
        ) #文本分割器的对象

    def upload_by_str(self,data:str,filename):
        """"将传入的字符串，进行向量化，存入向量数据库中"""
        md5= get_string_md5(data)
        if check_md5(md5):
            return "[跳过]文本已经存在数据库中"
        if len(data) >= config.max_split_char_number:
            knowledge_chunks = self.spliter.split_text(data)
        else:
            knowledge_chunks = [data]

        metadata ={
            "source":filename,
            "create_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator":"小名"
        }

        self.chroma.add_texts(
            knowledge_chunks,
            metadatas=[metadata for _ in knowledge_chunks])

        save_md5(md5)
        return "[成功]内容已经加载到向量库"




if __name__ == "__main__":
    service = KnowledgeBaseService()
    res = service.upload_by_str("周杰伦","testfile")
    print(res)

