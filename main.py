import sys
from pathlib import Path
# 将项目根目录加入Python搜索路径
sys.path.append(str(Path(__file__).parent))

from src.agent.customer_agent import EcommerceRAGAgent

if __name__ == "__main__":
    agent = EcommerceRAGAgent()
    agent.chat_loop()
