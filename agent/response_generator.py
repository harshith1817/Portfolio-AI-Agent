from llm.client import LLMClient

from agent.context_formatter import ContextFormatter
from agent.system_prompts.response_prompt import RESPONSE_SYSTEM_PROMPT


class ResponseGenerator:

    def __init__(self):
        self.llm = LLMClient()
        self.formatter = ContextFormatter()

    def generate(self, query: str, contexts: list) -> str:

        formatted_context = self.formatter.format(contexts)

        messages = [
            {
                "role": "system",
                "content": RESPONSE_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
User Question:
{query}

Available Context:

{formatted_context}

Instructions:
Answer the user's question using ONLY the provided context.
If the required information is unavailable, clearly state that you don't have enough information.
Do not mention internal tools such as GitHub, Resume, Portfolio, Planner, or Executor.
"""
            }
        ]

        return self.llm.generate(messages)