from core.config import GITHUB_PORTFOLIO_REPOSITORY
from clients.github_client import GitHubClient
from parsers.resume_parser import ResumeParser

class ResumeService:

    RESUME_PATH = "Frontend/src/pages/Resume/Resume.pdf"
    
    def __init__(self):
        self.client = GitHubClient()
        self.parser = ResumeParser()
        self._resume_cache = None

    def get_resume(self):

        if self._resume_cache is not None:
            return self._resume_cache

        pdf_bytes = self.client.get_file_bytes(
            repository_name=GITHUB_PORTFOLIO_REPOSITORY,
            path=self.RESUME_PATH
        )

        self._resume_cache = self.parser.parse(pdf_bytes)

        return self._resume_cache