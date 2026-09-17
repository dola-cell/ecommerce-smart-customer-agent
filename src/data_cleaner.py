import json
import re

def clean_product_text(text: str) -> str:
    # 去除换行、多余空格、特殊符号
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_spec(spec_str: str) -> dict:
    spec_dict = {}
    pairs = spec_str.split(", ")
    for p in pairs:
        if ":" in p:
            k, v = p.split(":", 1)
            spec_dict[k.strip()] = v.strip()
    return spec_dict

def clean_products(raw_path: str, out_path: str):
    with open(raw_path, "r", encoding="utf-8-sig") as f:
        raw_data = json.load(f)
    
    cleaned_list = []
    dirty_count = 0
    for item in raw_data:
        # 校验必填字段
        if not item.get("title") or not item.get("price"):
            dirty_count +=1
            continue
        
        cleaned = {}
        cleaned["product_id"] = item["product_id"]
        cleaned["title"] = clean_product_text(item["title"])
        cleaned["platform"] = item["platform"]
        cat_split = item["category"].split(" > ")
        cleaned["category_level1"] = cat_split[0]
        cleaned["category_level2"] = cat_split[1] if len(cat_split)>1 else cat_split[0]
        cleaned["specs"] = normalize_spec(item["spec"])
        cleaned["price"] = clean_product_text(item["price"])
        cleaned["description"] = clean_product_text(item["description"])
        cleaned_list.append(cleaned)
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_list, f, indent=2)
    print(f"✅清洗完成，有效商品：{len(cleaned_list)}，脏数据丢弃：{dirty_count}")

if __name__ == "__main__":
    clean_products("data/raw/raw_products.json", "data/cleaned/cleaned_products.json")
