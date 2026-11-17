from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool(description="获取体重，返回值是整数，单位是千克")
def get_weight()-> int:
    return 90

@tool(description="获取身高，返回值是整数，单位是厘米")
def get_height()-> int:
    return 172

agent = create_agent(
    model=ChatOpenAI(
        model="qwen3.8-27b",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"),
    tools=[get_height,get_weight],
    system_prompt="你是严格遵守React框架的智能体，必须按照【思考->行动->观察->再思考】的流程解决问题，且每轮仅能思考并调用1个工具，禁止单词调用多个工具，并告知我你的思考过程，工具调用的原因，按思考"
)

for chunk in agent.stream(
    {
        "messages":[
            {"role":"user","content":"计算我的bmi"}
        ]
    },
    stream_mode="values"
    ):
    latest_message = chunk['messages'][-1]

    if latest_message.content:
        print(type(latest_message).__name__,latest_message.content)

    try:
        if latest_message.tool_calls:
            print(f"工具调用：{ [tc['name'] for tc in latest_message.tool_calls] }")
    except AttributeError as e:
        pass