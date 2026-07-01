import json
import fitz

from utils.json_parser import JSONParser
from llm.client import LLMClient
from agent.system_prompts.resume_parser_prompt import (
    RESUME_PARSER_PROMPT,
)


class ResumeParser:

    def __init__(self):
        self.llm = LLMClient()

    def _extract_text(self, pdf_bytes: bytes):

        document = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    def parse(self, pdf_bytes: bytes):

        resume_text = self._extract_text(pdf_bytes)

        messages = [
            {
                "role": "system",
                "content": RESUME_PARSER_PROMPT
            },
            {
                "role": "user",
                "content": resume_text
            }
        ]

        response = self.llm.generate(messages)

        try:
            return JSONParser.parse(response)

        except Exception:

            return {
                "summary": resume_text
            }