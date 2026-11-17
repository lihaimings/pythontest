# from langchain_community.llms.tongyi import Tongyi
#
# model = Tongyi(model="qwen-plus")
#
# res = model.stream(input="你是谁呀")
#
# for chunk in res:
#     print(chunk,end=' ',flush=True)

from langchain_ollama import OllamaLLM
from langchain_core.prompts import  PromptTemplate

model = OllamaLLM(model="qwen3.5:4b")
pro = PromptTemplate.from_template("2025年的天气怎样")
chain = pro | model

res = chain.stream(input={})

res2 = model.invoke(input="你好啊")

print(type(res))

for item in res:
    print(item,end='',flush=True)
