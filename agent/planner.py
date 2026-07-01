import json

from llm.client import LLMClient
from agent.system_prompts.planner_prompt import PLANNER_SYSTEM_PROMPT
from utils.json_parser import JSONParser


class Planner:

    def __init__(self):
        self.llm = LLMClient()

    def plan(self, query: str):

        messages = [
            {
                "role": "system",
                "content": PLANNER_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": query
            }
        ]

        response = self.llm.generate(messages)

        try:
            return JSONParser.parse(response)

        except Exception:
            return {
                "plan": [],
                "error": "Planner returned invalid JSON.",
                "raw_response": response
            }