from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.customer_agent import EcommerceCustomerAgent

app = FastAPI(title="电商智能客服Agent")

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
def chat(req: ChatRequest):
    agent = EcommerceCustomerAgent()
    reply = agent.run(req.user_input)
    return {"reply": reply}

@app.post("/clear")
def clear_chat():
    agent = EcommerceCustomerAgent()
    agent.clear_history()
    return {"msg": "对话历史已清空"}

@app.get("/")
def root():
    return {"msg": "电商客服后端服务正常运行"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
