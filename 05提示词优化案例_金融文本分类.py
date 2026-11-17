from openai import OpenAI
from openai.resources.beta.threads import messages

# 1. 获取client
client = OpenAI(
    base_url="https://llm-d5qhjtm02b1v7vc0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)


examples_data = {
    '新闻报道':'今日，股市经历一轮震荡...',
    '财务报告':'本公司年度财务报告显示...',
    '公司公告':'本公司高兴的宣布完成一轮并购...',
    '分析师报告':'最新的分析报告指出...'
}

examples_types=['新闻报道','财务报告','公司公告','分析师报告']

#提问数据
questions = [
    "今日，央行发布公告宣布...",
    "anc公司今日发布公告....",
    "公司资产负载表显示....",
    "最新的分析报告指出....",
    "小明喜欢小新哦"
]

messages = [
    {"role":"system","content":"你是金融专家，将文本分类为['新闻报道','财务报告','公司公告','分析师报告']，不清楚的分析为不清楚"}
]

for key,value in examples_data.items():
    messages.append({"role":"user","content":value})
    messages.append({"role": "assistant", "content": key})

# print(messages)

for q in questions:
   response =  client.chat.completions.create(
        model="qwen3.8-flash",
        messages = messages+[{"role":"user","content":f"按照示例，回答这段文本分类：{q}"}],
    )

   print(response.choices[0].message.content)


