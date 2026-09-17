import json
from enum import Enum

class BadCaseType(Enum):
    KNOWLEDGE_MISS = "知识库缺失"
    RETRIEVE_ERROR = "召回错误"
    PROMPT_HALLUCINATION = "Prompt幻觉"
    TAG_ERROR = "标签匹配错误"

# 评测打分维度
EVAL_DIMENSIONS = ["accuracy", "relevance", "compliance"]

class AgentEvaluator:
    def __init__(self, test_query_path, bad_case_path):
        self.test_queries = json.load(open(test_query_path, "r", encoding="utf-8-sig"))
        self.bad_case_path = bad_case_path
        self.bad_cases = []

    def record_bad_case(self, query, model_name, case_type: BadCaseType, reason):
        case = {
            "query": query,
            "model": model_name,
            "type": case_type.value,
            "reason": reason
        }
        self.bad_cases.append(case)

    def export_report(self):
        with open(self.bad_case_path, "w", encoding="utf-8") as f:
            json.dump(self.bad_cases, f, indent=2)
        # 统计各类bad case数量
        stat = {}
        for item in self.bad_cases:
            t = item["type"]
            stat[t] = stat.get(t,0)+1
        print("\n===== Bad Case 量化统计报告 =====")
        for k,v in stat.items():
            print(f"{k}: {v} 个，占比 {v/len(self.bad_cases)*100:.1f}%")
        return stat

if __name__ == "__main__":
    evaluator = AgentEvaluator("data/test_queries.json","data/bad_case_store.json")
    # ========== 在这里手动填入你的模型评测结果（Demo演示用） ==========
    evaluator.record_bad_case(
        query="Find a ski jacket under $500",
        model_name="GPT-4o",
        case_type=BadCaseType.KNOWLEDGE_MISS,
        reason="知识库没有滑雪夹克商品，模型仍然推荐产品，产生幻觉"
    )
    evaluator.export_report()
