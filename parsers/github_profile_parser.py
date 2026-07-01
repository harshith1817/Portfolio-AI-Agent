from llm.client import LLMClient

from utils.json_parser import JSONParser
from agent.system_prompts.github_profile_prompt import (
    GITHUB_PROFILE_PROMPT
)


class GitHubProfileParser:

    def __init__(self):
        self.llm = LLMClient()

    def parse(self, readme: str):

        messages = [
            {
                "role": "system",
                "content": GITHUB_PROFILE_PROMPT
            },
            {
                "role": "user",
                "content": readme
            }
        ]

        response = self.llm.generate(messages)

        return JSONParser.parse(response)