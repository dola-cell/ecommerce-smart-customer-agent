from app.agents.base_agent import BaseAgent
from app.core.config import settings

class EcommerceCustomerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            api_key=settings.LLM_API_KEY,
            base_url=settings.LLM_BASE_URL,
            model_name=settings.LLM_MODEL
        )

    def clear_history(self):
        self.history = []

    def run(self, user_input: str):
        return self.llm_call(user_input)
