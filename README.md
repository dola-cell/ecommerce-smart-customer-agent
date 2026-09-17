
# Cross-border E-commerce AI Shopping Guide Agent

> 
> AI 电商商品导购 Agent｜适配海外 Temu/Amazon 跨境场景
> 项目定位：AI 电商产品实习项目，完整覆盖商品知识库建设、数据清洗、Prompt 迭代、多模型评测与 Bad Case 量化归因。

## 📌 Project Background

Overseas cross-border e-commerce users face difficulty selecting goods from massive product inventory.
This AI Agent acts as a shopping guide for US consumers, retrieving products from standardized commodity knowledge base, answering product specs and making recommendations.

## 📊 Competitor Analysis

See full report: [competitor_analysis.md](./product_docs/competitor_analysis.md)
Key pain point of existing AI shopping assistant: LACK of standardized product knowledge base, easy to produce LLM hallucination.

## 🧩 Product Design

### 1. Commodity Knowledge Base & Data Standard

- Raw overseas product data from Temu & Amazon
- Data cleaning script: remove noise, unify unit, filter dirty data
- Multi-level category + attribute tag system
Data spec: [data_spec.md](./product_docs/data_spec.md)

### 2. Agent Workflow

User English Query → Query understanding → RAG retrieve products from knowledge base → Prompt constraint → LLM response → Record case for evaluation

### 3. Prompt Iteration History

- V1: Simple prompt, easy hallucination
- V2: Add role & basic constraint
- V3 Final Version: Hard rule + fixed output format, limit model to only use knowledge base data

### 4. Evaluation Framework & Bad Case Analysis (Core Module)

- Test dataset: 25 real user English shopping queries
- Evaluate GPT-4o / Gemini / Claude on 3 metrics: Accuracy, Relevance, Compliance
- Auto classify bad case into 4 types:
  1. 知识库缺失
  2. 召回错误
  3. Prompt 幻觉
  4. 标签匹配错误
- Output quantitative statistic report to support product iteration

## 🖼️ Demo Screenshot

## 📁 Project Structure

```
├── data/                    # 商品数据集 & 评测集
├── product_docs/            # Product documents: PRD, competitor analysis
├── src/
│   ├── data_cleaner.py      # Data cleaning & structuring
│   ├── tag_builder.py       # Product tag system
│   ├── agent.py             # AI导购Agent主逻辑
│   └── evaluator.py         # Multi-model evaluation & bad case analysis
└── README.md
```

## 🚀 Quick Start

```
# 1. Clean raw product data
python src/data_cleaner.py
# 2. Build product tags
python src/tag_builder.py
# 3. Run evaluation & bad case statistics
python src/evaluator.py
```

## 📋 Product PRD

[product_prd.md](./product_docs/product_prd.md)

## ✨ Project Summary

This project fully simulates the daily work of AI E-commerce Product Intern(Product direction):

1. Build commodity knowledge base, data cleaning & quality check
2. Overseas e-commerce competitor research
3. AI Agent product design, Prompt engineering
4. Multi-model evaluation, bad case quantitative analysis and product iteration.
