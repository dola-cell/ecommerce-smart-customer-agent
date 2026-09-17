# 商品数据Schema规范（产品定义）
```json
{
  "product_id": "唯一商品ID",
  "title": "商品英文标题",
  "platform": "来源平台：Temu / Amazon / Shopify",
  "category_level1": "一级类目",
  "category_level2": "二级类目",
  "specs": {"Capacity":"40L","Material":"Nylon"},
  "tags": ["Waterproof","Nylon"],
  "price": "79.99 USD",
  "description": "商品英文描述"
}
## 数据清洗规则

1. 去除多余换行、HTML 符号
2. 统一单位格式
3. 必填字段缺失 → 判定脏数据丢弃

## 标签体系

一级类目 > 二级类目 > 属性标签
