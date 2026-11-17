from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("我的邻居姓{name},刚生了{gender},名字不能包含[明、海、敏、夏、桂、强、群、秀],你帮我取个名字，简单回答")

# prompt_text = prompt_template.format(name="李", gender="女孩")
# print(prompt_text)

# model = Tongyi(model="qwen-plus")
# res = model.invoke(input=prompt_text)
# print(res)

model = Tongyi(model="qwen-plus")
chain = prompt_template | model
res = chain.invoke(input={"name":"张","gender":"女儿"})
print(res)
