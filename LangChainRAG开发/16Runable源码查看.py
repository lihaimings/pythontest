from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain_core.runnables import RunnableSequence

prompt = PromptTemplate.from_template("现在多少点了")

model = Tongyi(model="qwen-plus")

chain = prompt | model # RunnableSequence

print(type(chain))


print(chain.invoke({}))
