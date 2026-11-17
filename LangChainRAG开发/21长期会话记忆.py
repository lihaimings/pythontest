import os,json
from collections.abc import Sequence
from langchain_core.messages import message_to_dict,messages_from_dict,BaseMessage
from  langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id = session_id
        self.storage_path = storage_path
        #完整文件路径
        self.file_path = os.path.join(self.storage_path,self.session_id)
        #确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self,messages:Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        #将数据同步到本地文件中
        new_messages = [message_to_dict(message) for message in all_messages]
        # 将数据写入到文件
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump(new_messages,f)

    @property # @property装饰器将messages方法变成成员属性用
    def messages(self)-> list[BaseMessage]:
        try:
            with open(self.file_path,"r",encoding="utf-8") as f:
                messages_data= json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)




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


def get_histor(session_id):
    return FileChatMessageHistory(session_id,"./chat_history")

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

    # res = conversation_chain.invoke({"input":"小明有2只猫"},session_config)
    # print("第一次执行",res)
    #
    # res = conversation_chain.invoke({"input":"小红有1只猫"},session_config)
    # print("第二次执行",res)

    res = conversation_chain.invoke({"input":"一共有多少只猫"},session_config)
    print("第三次执行",res)
