import chromadb
import json
from src.common.logger import logger
from pathlib import Path

class ProductVectorStore:
    def __init__(self, persist_dir: str):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.collection = self.client.get_or_create_collection(name="ecommerce_product")

    def build(self, product_path: str):
        with open(product_path, "r", encoding="utf-8") as f:
            products = json.load(f)

        docs = []
        ids = []
        meta = []
        for p in products:
            text = f"{p['name']} {p['desc']} {p['category']}"
            docs.append(text)
            ids.append(p["id"])
            meta.append({"price": p["price"]})

        self.collection.add(documents=docs, ids=ids, metadatas=meta)
        logger.info(f"✅向量库构建完成，共{len(docs)}条商品")

    def search(self, query: str, top_k: int=3):
        res = self.collection.query(query_texts=[query], n_results=top_k)
        return res

if __name__ == "__main__":
    vs = ProductVectorStore("data/vector_db")
    vs.build("data/processed/cleaned_products.json")
