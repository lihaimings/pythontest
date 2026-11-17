from typing import Optional
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.embeddings import Embeddings
from langchain_openai import ChatOpenAI
from langchain_openai.chat_models.base import BaseChatOpenAI
from abc import ABC,abstractmethod


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self)-> Optional[Embeddings | BaseChatOpenAI]:
        pass

class ChatModelFactory(BaseModelFactory):
    def generator(self)-> Optional[Embeddings | BaseChatOpenAI]:
        return ChatOpenAI(
        model="qwen4-max",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")


class EmbeddingsFactory(BaseModelFactory):
    def generator(self)-> Optional[Embeddings | BaseChatOpenAI]:
        return DashScopeEmbeddings()

embed_model = EmbeddingsFactory().generator()
chat_model = ChatModelFactory().generator()

