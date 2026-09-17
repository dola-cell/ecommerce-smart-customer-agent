# test_key.py
from dotenv import load_dotenv
import os

# 加载当前目录的 .env 文件
load_dotenv()

# 读取你.env里面的 LLM_API_KEY
api_key = os.getenv("LLM_API_KEY")

if not api_key:
    print("❌ 没有读到 LLM_API_KEY，请确认 .env 文件存在，并且里面写了 LLM_API_KEY=xxxx")
else:
    try:
        header_value = f"Bearer {api_key}"
        header_value.encode("latin-1")
        print("✅ 密钥可以 latin-1 编码，密钥字符没问题！")
    except Exception as e:
        print(f"❌ 密钥包含 latin1 不支持的字符！报错信息：{e}")
