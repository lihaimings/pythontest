from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool(description="查询天气")
def get_weather()-> str:
    return "晴天"

agent = create_agent(
    model=ChatOpenAI(
        model="qwen3.8-27b",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"),
    tools=[get_weather],
    system_prompt="你是一个聊天助手，可以回答用户问题"
)

res = agent.invoke(
    {
        "messages":[
            {"role":"user","content":"明天深圳的天气如何？"}
        ]
    }
)

for message in res["messages"]:
    print(type(message).__name__,message.content)