from pathlib import Path

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path=str(Path(__file__).resolve().parent / "data" / "stu.csv"),
    csv_args={
        "delimiter": ",", # 指定分隔符
        "quotechar": '"', # 指定带有分割符文本的引号包围是单引号还是双引号
        # 替代数据表头
        "fieldnames":['name','age','gender','兴趣']
    },
    encoding="utf-8"
)

# load批量加载
# documents = loader.load()
#
# for document in documents:
#     print(type(document))
#     print(document)

#懒加载 lazy_load
for doc in loader.lazy_load():
    print(doc)
