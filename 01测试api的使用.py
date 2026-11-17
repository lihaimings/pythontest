from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    base_url="https://llm-d5qhjtm02b1v7vc0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

response= client.chat.completions.create(
    model="qwen3.5:4b",
    messages=[
        {"role":"system","content":"你是一个python编程专家"},
        {"role":"assistant","content":"你好我是编程专家"},
        {"role":"user","content":"你能做什么"}
    ]
)

print("model",response.model)
print("content",response.choices[0].message.content)




messages = [{"role": "user", "content": "你能做什么"}]
completion = client.chat.completions.create(
    model="deepseek-v4-flash-0731",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)
is_answering = False  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)