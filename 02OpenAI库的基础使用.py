from openai import OpenAI

# 1. 获取client
client = OpenAI(
    base_url="https://llm-d5qhjtm02b1v7vc0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

# 2. 模型调用
response = client.chat.completions.create(
    model="qwen3.8-flash",
    messages=[
        { "role":"system","content":"您是python编程专家，并且不说废话简单回答"},
        {"role": "assistant", "content": "你好，我是python编程专家"},
        {"role": "user", "content": "输出1-10的数字，使用python代码"}
    ]
)

# 3.处理结果
print(response.choices[0].message.content)