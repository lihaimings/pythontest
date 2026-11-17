import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

str_parser = StrOutputParser()
model = ChatOpenAI(
    model="qwen3.8-27b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我的邻居姓：{lastname}，刚生了{gender},请帮忙起名字，并封装成json格式返回给我。要求key是name,value是名字"
)


# 第二个提示词模板
two_prompt = PromptTemplate.from_template(
    "姓名：{name}，请解析名字的含义"
)

# ChatOpenAI 返回 AIMessage，将消息中的 JSON 解析成包含 name 的字典。
my_func = RunnableLambda(lambda message: {"name":message})

chain = first_prompt | model | my_func | two_prompt | model | str_parser


# print(chain.stream({"lastname":"李","gender":"男"}))

for i in chain.stream({"lastname":"李","gender":"男"}):
    print(i, end="", flush=True)
print()
