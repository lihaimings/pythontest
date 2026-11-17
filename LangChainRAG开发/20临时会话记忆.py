from langchain_core.prompts import PromptTemplate,MessagesPlaceholder,ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

str_parser = StrOutputParser()
model = ChatOpenAI(
    model="qwen3.8-27b",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# prompt_template = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题，对话历史：{chat_history},用户提问：{input} ，请回答"
# )


prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你需要根据会话历史回应用户问题，对话历史:"),
        MessagesPlaceholder("chat_history"),
        ("human","请回答如下问题：{input}")
    ]
)


def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt

base_chain = prompt_template | print_prompt | model |str_parser


store={}

def get_histor(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

conversation_chain = RunnableWithMessageHistory(
    base_chain, #被增强的原有的chain
    get_histor, # 通过会话id获取InMemoryChatMessageHistory
    input_messages_key="input", # 表示用户输入再模板中的占位符
    history_messages_key="chat_history" # 表示用户输入再模板中的占位符
)

if __name__ == "__main__":
    session_config = {
        "configurable":{
            "session_id":"user_001"
        }
    }

    res = conversation_chain.invoke({"input":"小明有2只猫"},session_config)
    print("第一次执行",res)

    res = conversation_chain.invoke({"input":"小红有1只猫"},session_config)
    print("第二次执行",res)

    res = conversation_chain.invoke({"input":"一共有多少只猫"},session_config)
    print("第三次执行",res)