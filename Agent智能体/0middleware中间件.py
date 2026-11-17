from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_tool_call, \
    wrap_model_call
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.runtime import Runtime


@tool(description="查询天气")
def get_weather(city:str)-> str:
    return f"{city}天气是：晴天"

"""
agent执行前后
model执行前后
工具执行中
模型执行中
"""

@before_agent
def log_before_agent(state:AgentState,runtime:Runtime):
    print(f"[before agent]agent启动，并附带{len(state['messages'])}消息")


@after_agent
def log_after_agent(state:AgentState,runtime:Runtime):
    print(f"[after agent]agent结束，并附带{len(state['messages'])}消息")


@before_model
def log_before_model(state:AgentState,runtime:Runtime):
    print(f"[before model]模型启动，并附带{len(state['messages'])}消息")


@after_model
def log_after_model(state:AgentState,runtime:Runtime):
    print(f"[after model]模型结束，并附带{len(state['messages'])}消息")

@wrap_model_call
def model_call(request,handler):
    print("模型调用")
    return handler(request)


@wrap_tool_call
def log_tool_call(request,handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具执行传入的参数{request.tool_call['args']}")
    return handler(request)

agent = create_agent(
    model=ChatOpenAI(
        model="qwen3.8-27b",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"),
    tools=[get_weather],
    middleware=[log_before_agent, log_after_agent, model_call, log_tool_call,log_before_model,log_after_model],
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