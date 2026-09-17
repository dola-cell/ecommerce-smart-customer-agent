# E-commerce Smart Customer Agent
AI电商智能客服项目

## 项目简介
本项目实现面向电商场景的AI商品咨询助手，包含商品数据清洗、标签自动构建、用户问答评测模块。
- 对原始商品JSON数据做清洗，过滤脏数据
- 自动抽取商品标签，用于检索召回
- 用户Query评测模块，自动统计模型回答Bad Case，量化效果

## 项目结构
├── data/
│   ├── raw/                # 原始商品数据
│   ├── cleaned/            # 清洗后带标签商品数据
│   ├── test_queries.json   # 用户测试问句
│   └── bad_case_store.json # 评测失败案例存储
├── src/
│   ├── data_cleaner.py     # 商品数据清洗脚本
│   ├── tag_builder.py      # 商品标签构建脚本
│   └── evaluator.py        # 问答效果评测脚本
├── product_docs/           # 产品文档：PRD、竞品分析、数据规范
├── .gitignore              # 忽略虚拟环境、缓存文件
└── README.md

```

## 环境安装
```bash
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 安装依赖（后续补充requirements.txt）
pip install -r requirements.txt
```

## 运行方式

1. 商品数据清洗

```
python src/data_cleaner.py
```

2. 商品标签构建

```
python src/tag_builder.py
```

3. 模型问答效果评测

```
python src/evaluator.py
```

## 项目亮点

1. 模块化设计：数据处理、标签构建、评测解耦，方便迭代扩展
2. Bad Case 自动收集：记录回答失败的用户 query，用于迭代 Prompt
3. 标准化数据规范，配套 PRD 与竞品分析文档，贴合真实产品开发流程

## 后续规划

- 实现对话 Agent 主逻辑，接入大模型完成商品问答
- 增加评测结果可视化图表
- 增加向量检索，支持商品知识库召回
