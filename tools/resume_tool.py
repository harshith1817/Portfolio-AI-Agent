from tools.base_tool import BaseTool
from services.resume_service import ResumeService


class ResumeTool(BaseTool):

    def __init__(self):
        self.service = ResumeService()

    def execute(self, action: str, parameters: dict):

        resume = self.service.get_resume()

        if action == "summary":
            return resume

        if action in resume:
            return resume[action]

        raise ValueError(f"Unsupported Resume action: {action}")