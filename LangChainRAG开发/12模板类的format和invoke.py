from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate,ChatPromptTemplate

""""
PromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
FewShotPromptTemplate -> StringPromptTemplate -> BasePromptTemplate-> RunnableSerializable -> Runnable
ChatPromptTemplate -> BaseChatPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
"""

template = PromptTemplate.from_template("我的邻居是{name}")

res = template.format(name="小明")
print(res,type(res))

res2 = template.invoke({"name":"小红"})
print(res2,type(res2))