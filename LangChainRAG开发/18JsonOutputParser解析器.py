from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

str_parser = StrOutputParser()
json_parser = JsonOutputParser()
model = ChatTongyi(model="qwen-plus")

# 第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我的邻居姓：{lastname}，刚生了{gender},请帮忙起名字，并封装成json格式返回给我。要求key是name,value是名字"
)


# 第二个提示词模板
two_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义"
)

chain = first_prompt | model | json_parser | two_prompt | model | str_parser


print(chain.invoke({"lastname":"李","gender":"男"}))
