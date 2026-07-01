from agent.planner import Planner
from agent.executor import Executor
from agent.response_generator import ResponseGenerator


class PortfolioAgent:

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.response_generator = ResponseGenerator()

    def chat(self, query: str) -> dict:
        """
        Complete Agent Pipeline

        User Query
            ↓
        Planner
            ↓
        Execution Plan
            ↓
        Executor
            ↓
        Retrieved Context
            ↓
        Response Generator
            ↓
        Final Response
        """

        # Step 1: Generate execution plan
        plan = self.planner.plan(query)

        # Planner failed
        if "error" in plan:
            return {
                "success": False,
                "answer": "I'm sorry, I couldn't understand your request.",
                "plan": plan,
                "contexts": []
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