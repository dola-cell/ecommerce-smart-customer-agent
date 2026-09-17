"""
LLM 抽象客户端
支持切换不同大模型，本地Mock用于演示，可替换为通义千问/OpenAI等API
"""
from src.common.logger import logger

class BaseLLMClient:
    def chat(self, prompt: str) -> str:
        raise NotImplementedError

class MockLLMClient(BaseLLMClient):
    """本地模拟大模型，演示使用；项目上线替换为真实API"""
    def chat(self, prompt: str) -> str:
        logger.info(f"LLM收到prompt:\n{prompt}")
        return f"【AI客服回答】根据商品知识库：\n{prompt}\n\n> 温馨提示：该回答来自Mock大模型，可接入真实大模型API。"

# 工厂函数，方便切换模型
def get_llm_client(model_name: str):
    if model_name == "mock":
        return MockLLMClient()
    else:
        raise ValueError(f"不支持的模型 {model_name}")

if __name__ == "__main__":
    llm = get_llm_client("mock")
    print(llm.chat("你好"))
