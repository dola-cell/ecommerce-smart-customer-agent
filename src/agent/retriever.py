from src.data_pipeline.vector_store import ProductVectorStore
from src.common.logger import logger

class ProductRetriever:
    def __init__(self, vector_db_path: str, top_k: int = 3):
        self.vs = ProductVectorStore(vector_db_path)
        self.top_k = top_k

    def retrieve(self, query: str):
        res = self.vs.search(query, top_k=self.top_k)
        # 整理召回结果
        docs = res.get("documents", [[]])[0]
        ids = res.get("ids", [[]])[0]
        logger.info(f"检索query={query}, 召回数量={len(docs)}")
        return list(zip(ids, docs))

if __name__ == "__main__":
    r = ProductRetriever("data/vector_db", top_k=3)
    print(r.retrieve("防晒衣服"))
