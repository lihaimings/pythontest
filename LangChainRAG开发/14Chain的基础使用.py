from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi


chat = ChatPromptTemplate.from_messages(
    [
        ("system","你是一个边塞诗人,简易回答"),
        MessagesPlaceholder("history"),
        ("human","请再来一首唐诗")
    ]
)

history_data = [
    ("human","你来写一首唐诗"),
    ("ai","床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human","好诗再来一个"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
]

# prompt_text = chat.invoke({"history":history_data})

model = ChatTongyi(model="qwen-plus",streaming=True)

chain = chat | model

# print(chain.invoke({"history":history_data}).content)

for chunk in chain.stream({"history":history_data}):
    print(chunk.content,end='',flush=True)

