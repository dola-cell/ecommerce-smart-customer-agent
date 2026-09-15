# base_agent.py 完整版，兼容旧参数model_name，DeepSeek专用，解决latin1编码报错
from abc import ABC
import json
import http.client
import urllib.parse
from app.core.config import settings

class BaseAgent(ABC):
    def __init__(self, api_key=None, base_url=None, model=None, model_name=None):
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = settings.LLM_API_KEY

        if base_url:
            self.base_url = base_url.strip().rstrip("/")
        else:
            self.base_url = settings.LLM_BASE_URL.strip().rstrip("/")

        # 优先model，其次model_name（适配你旧代码传参model_name）
        if model:
            self.model = model
        elif model_name:
            self.model = model_name
        else:
            self.model = settings.LLM_MODEL

        self.history = []

    def llm_call(self, user_prompt: str):
        self.history.append({"role": "user", "content": user_prompt})
        payload = {
            "model": self.model,
            "messages": self.history
        }
        payload_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")

        url_parts = urllib.parse.urlparse(self.base_url)
        host = url_parts.netloc
        path_prefix = url_parts.path
        req_path = f"{path_prefix}/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json; charset=utf-8",
            "Content-Length": str(len(payload_bytes))
        }
        try:
            conn = http.client.HTTPSConnection(host, timeout=30)
            conn.request("POST", req_path, body=payload_bytes, headers=headers)
            resp = conn.getresponse()
            raw_body = resp.read()
            conn.close()

            if resp.status >= 400:
                text = raw_body.decode("utf-8", errors="ignore")
                raise Exception(f"请求失败 status={resp.status}, body: {text}")

            result_data = json.loads(raw_body.decode("utf-8"))
            reply = result_data["choices"][0]["message"]["content"]
            self.history.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            raise Exception(f"调用DeepSeek大模型失败：{str(e)}")
