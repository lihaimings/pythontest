from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3.5:4b")

res = model.invoke(input="你是谁")

print(res)

