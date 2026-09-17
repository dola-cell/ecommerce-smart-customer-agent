"""
企业版数据清洗模块
Pydantic做数据校验，结构化输出，日志记录脏数据
"""
import json
from pathlib import Path
from pydantic import BaseModel, Field
from src.common.logger import logger

class ProductSchema(BaseModel):
    id: str
    name: str = Field(min_length=1)
    desc: str
    price: float = Field(gt=0)
    category: str

def run_clean(raw_path: str, out_path: str):
    raw_file = Path(raw_path)
    out_file = Path(out_path)
    out_file.parent.mkdir(exist_ok=True, parents=True)

    with open(raw_file, "r", encoding="utf-8") as f:
        raw_list = json.load(f)

    valid = []
    invalid_count = 0
    for item in raw_list:
        try:
            prod = ProductSchema(**item)
            valid.append(prod.model_dump())
        except Exception as e:
            invalid_count +=1
            logger.warning(f"脏数据丢弃: {item}, err:{str(e)}")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(valid, f, ensure_ascii=False, indent=2)

    logger.info(f"✅清洗完成，有效商品:{len(valid)}，脏数据:{invalid_count}")
    return valid

if __name__ == "__main__":
    run_clean("data/raw/products.json", "data/processed/cleaned_products.json")
