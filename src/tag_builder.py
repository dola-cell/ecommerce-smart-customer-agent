import json

def build_tags(product: dict) -> list:
    tags = []
    # 类目标签
    tags.append(product["category_level1"])
    tags.append(product["category_level2"])
    # 属性标签
    specs = product["specs"]
    if "Material" in specs:
        tags.append(specs["Material"])
    return list(set(tags))

if __name__ == "__main__":
    with open("data/cleaned/cleaned_products.json","r",encoding="utf-8-sig") as f:
        products = json.load(f)
    for p in products:
        p["tags"] = build_tags(p)
    with open("data/cleaned/cleaned_products.json","w",encoding="utf-8") as f:
        json.dump(products,f,indent=2)
    print("✅标签体系构建完成")
