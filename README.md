\# E-Commerce Smart Customer Agent



> 

> 基于大模型构建的电商智能客服 Agent，FastAPI 后端，支持多轮对话上下文记忆，对接 DeepSeek LLM API。



\## ✨ Features



\- 多轮对话：自动维护对话历史，Agent 具备上下文记忆能力，连贯回答用户咨询

\- 电商场景定制：适配发货时间、物流查询、退换货、订单问题等客服场景

\- 兼容旧业务代码：基类做参数兼容，最小改动接入已有客服业务逻辑

\- 规避编码异常：使用原生 `http.client` 替代 requests，解决 OpenAI 兼容接口常见 latin1 header 解码报错

\- 轻量 Web API：基于 FastAPI，内置 Swagger UI 在线调试接口，开箱即可测试



\## 📦 Project Structure



```

backend/

├── app/

│   ├── agents/

│   │   ├── base\_agent.py          # Agent 抽象基类，封装 LLM 调用、对话历史管理

│   │   └── customer\_agent.py      # 电商客服业务 Agent，继承 BaseAgent

│   └── core/

│       └── config.py              # 环境配置：LLM API Key、BaseURL、模型名称

└── main.py                        # FastAPI 入口，定义 /chat 对话接口

```



\## 🛠 Environment



Python >= 3.9



```

pip install fastapi uvicorn pydantic

```



\## ⚙ Config



在 `app/core/config.py` 中配置大模型信息：



```

from pydantic\_settings import BaseSettings



class Settings(BaseSettings):

&#x20;   LLM\_API\_KEY: str = "your-api-key"

&#x20;   LLM\_BASE\_URL: str = "https://api.deepseek.com/v1"

&#x20;   LLM\_MODEL: str = "deepseek-chat"



settings = Settings()

```



\## 🚀 Run



```

\# 启动服务（不带热重载，消除 reload 触发的参数警告）

uvicorn main:app

```



访问：`http://127.0.0.1:8000/docs` 进入 Swagger UI，直接在线调试 `/chat` 接口。



\### API



\- POST `/chat`

Request Body



```

{

&#x20; "user\_input": "你好，请问商品什么时候发货？"

}

```



Response



```

{

&#x20; "reply": "模型返回的客服应答内容"

}

```



\## 📝 Core Technical Solution



> 

> 问题：DeepSeek API 返回的 HTTP 响应头包含非 ASCII 字符，`requests` 库解析 headers 时抛出 `UnicodeDecodeError: latin1`。

> 方案：放弃 requests/httpx，使用 Python 内置 `http.client`，仅读取响应二进制 body，不解析响应头，绕过编码异常；基类增加参数兼容，保留原有业务 Agent 的调用方式，低侵入改造。



\## 📌 Demo



1\. 调用 `/chat` 发起首轮咨询，询问发货时间

2\. 继续传入后续对话，Agent 读取历史上下文进行连贯应答

3\. 可扩展：增加工具调用（订单查询接口）、意图分类、敏感词过滤等模块

