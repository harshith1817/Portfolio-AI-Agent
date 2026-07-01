from groq import Groq

from core.config import GROQ_API_KEY
from llm.models import DEFAULT_MODEL, TEMPERATURE, MAX_TOKENS


class LLMClient:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, messages):

        response = self.client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )

        return response.choices[0].message.content