"""
企业级电商客服Agent
RAG流程：用户Query -> 向量检索召回商品 -> 组装上下文Prompt -> LLM生成回答
"""
import yaml
from src.agent.retriever import ProductRetriever
from src.agent.llm_client import get_llm_client
from src.common.logger import logger

def load_config():
    with open("config/settings.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

class EcommerceRAGAgent:
    def __init__(self):
        cfg = load_config()
        self.retriever = ProductRetriever(
            vector_db_path=cfg["paths"]["vector_db"],
            top_k=cfg["retrieval"]["top_k"]
        )
        self.llm = get_llm_client(cfg["llm"]["model_name"])

    def build_prompt(self, user_query: str, context_docs):
        context_text = "\n".join([doc for _, doc in context_docs])
        prompt = f"""
你是专业电商客服，只能基于下面商品知识库回答用户问题，不要编造不存在商品。
【商品知识库】
{context_text}

【用户问题】
{user_query}

要求：回答简洁友好，如果知识库没有相关商品，如实告知用户。
"""
        return prompt

    def chat(self, user_query: str):
        # 1.向量检索
        docs = self.retriever.retrieve(user_query)
        # 2.构造prompt
        prompt = self.build_prompt(user_query, docs)
        # 3.调用大模型生成回答
        answer = self.llm.chat(prompt)
        return answer

    def chat_loop(self):
        print("===== 企业版RAG电商客服启动 | 输入 quit 退出 =====")
        while True:
            user_input = input("\n用户：")
            if user_input.strip().lower() == "quit":
                logger.info("对话结束")
                print("客服：感谢咨询，再见！")
                break
            ans = self.chat(user_input)
            print(f"客服：{ans}")

if __name__ == "__main__":
    agent = EcommerceRAGAgent()
    agent.chat_loop()
