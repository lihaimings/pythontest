from openai import OpenAI

# 1. 获取client
client = OpenAI(
    base_url="https://llm-d5qhjtm02b1v7vc0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

# 2. 模型调用
response = client.chat.completions.create(
    model="qwen3.8-flash",
    messages=[
        { "role":"system","content":"你是AI助理，回答很简洁"},
        {"role": "user", "content": "小敏有两条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有3只宠物猫"},
        {"role": "assistant", "content": "一共有多少宠物？"},
    ],
    stream=True  #开启流式输出功能
)

# 3.处理结果
# print(response.choices[0].message.content)
for chunk in response:
    if not chunk.choices:
        continue
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end="", flush=True)
