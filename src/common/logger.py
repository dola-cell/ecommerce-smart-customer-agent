from loguru import logger
import sys

# 企业级日志配置
logger.remove()
logger.add(sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")
logger.add("logs/runtime.log", rotation="500 MB", retention="10 days", level="INFO")

if __name__ == "__main__":
    logger.info("Logger init success")
