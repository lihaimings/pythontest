from pathlib import Path

from langchain_community.document_loaders import JoplinLoader, JSONLoader

# loader = JSONLoader(
#     file_path="./data/stu.json",
#     jq_schema="." , #提取字段， .默认整个
#     text_content=False, #提取字段是否字符串，默认true
# )
#
# loader = JSONLoader(
#     file_path="./data/stus.json",
#     jq_schema=".[].name" , #提取字段， .默认整个
#     text_content=False, #提取字段是否字符串，默认true
# )

loader = JSONLoader(
    file_path=str(Path(__file__).resolve().parent / "data" / "stus_line.json"),
    jq_schema=".name" , #提取字段， .默认整个
    text_content=False, #提取字段是否字符串，默认true
    json_lines=True
)



doc = loader.load()
print(doc)
