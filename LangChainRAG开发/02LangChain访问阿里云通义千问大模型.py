from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-plus")

res = model.invoke(input="你是谁呀？能做什么")


print(res)

