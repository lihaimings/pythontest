from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatTongyi(model="qwen-plus",streaming=True)

messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当苦，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    HumanMessage(content="按照你上一个回复的格式：写一首唐诗")
]

res = model.stream(input=messages)

for msg in res:
    print(msg.content,end='',flush=True)