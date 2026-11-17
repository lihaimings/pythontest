from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
prompt = PromptTemplate.from_template("现在多少点了{name}")

model = ChatTongyi(model="qwen-plus")

chain = prompt | model |parser| model

print(chain.invoke({"name":"谢谢你"}).content)
