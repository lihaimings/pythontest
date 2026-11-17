from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./data/kk.pdf",
    mode="single", # 默认page以页为单位,single只返回一个
    # password=""  文档密码
)

i= 0
for doc in loader.lazy_load():
    i+=1
    print(doc)
    print("="*20,i)