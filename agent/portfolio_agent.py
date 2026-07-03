from agent.planner import Planner
from agent.executor import Executor
from agent.response_generator import ResponseGenerator


class PortfolioAgent:

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.response_generator = ResponseGenerator()

    def chat(self, query: str) -> dict:

        # Step 1: Generate execution plan
        plan = self.planner.plan(query)

        if not plan.get("plan"):
            return {
                "success": True,
                "answer": (
                    "I mainly answer questions about Harshith, his background, "
                    "skills, projects, and experience. I don't have information "
                    "about that topic."
                )
            }

        # Step 2: Execute tool calls
        contexts = self.executor.execute(plan)

        # Step 3: Generate final answer
        answer = self.response_generator.generate(
            query=query,
            contexts=contexts
        )

        return {
            "success": True,
            "answer": answer,
            "plan": plan,
            "contexts": contexts
        }