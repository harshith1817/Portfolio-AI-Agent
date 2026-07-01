import base64
import requests

from core.config import GITHUB_TOKEN, GITHUB_USERNAME


class GitHubClient:

    BASE_URL = "https://api.github.com"
    TIMEOUT = 10

    def __init__(self):

        self.headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json"
        }

    def _get(self, endpoint: str):
        """
        Generic GET request to the GitHub REST API.
        """

        response = requests.get(
            f"{self.BASE_URL}{endpoint}",
            headers=self.headers,
            timeout=self.TIMEOUT
        )

        response.raise_for_status()

        return response.json()

    # ----------------------------------------------------
    # Repository APIs
    # ----------------------------------------------------

    def get_repositories(self):
        """
        Fetch all repositories for the configured user.
        """

        return self._get(
            f"/users/{GITHUB_USERNAME}/repos"
        )

    def get_repository(self, repository_name: str):
        """
        Fetch metadata for a repository.
        """

        return self._get(
            f"/repos/{GITHUB_USERNAME}/{repository_name}"
        )

    def get_languages(self, repository_name: str):
        """
        Fetch programming languages used in a repository.
        """

        return self._get(
            f"/repos/{GITHUB_USERNAME}/{repository_name}/languages"
        )

    def get_readme(self, repository_name: str):
        """
        Fetch the README metadata.

        Content is Base64 encoded.
        Decoding is handled by the service layer.
        """

        return self._get(
            f"/repos/{GITHUB_USERNAME}/{repository_name}/readme"
        )

    # ----------------------------------------------------
    # Generic File APIs
    # ----------------------------------------------------

    def get_file_content(
        self,
        repository_name: str,
        path: str,
        branch: str = "main"
    ):
        """
        Fetch any file from a GitHub repository.

        Returns the raw GitHub Contents API response.

        The 'content' field is Base64 encoded.
        Decoding should be performed by the service layer.
        """

        return self._get(
            f"/repos/{GITHUB_USERNAME}/{repository_name}/contents/{path}?ref={branch}"
        )

    def get_file_text(
        self,
        repository_name: str,
        path: str,
        branch: str = "main"
    ):
        """
        Fetch a text file and return the decoded UTF-8 content.
        """

        response = self.get_file_content(
            repository_name=repository_name,
            path=path,
            branch=branch
        )

        return base64.b64decode(
            response["content"]
        ).decode("utf-8")

    def get_file_bytes(
        self,
        repository_name: str,
        path: str,
        branch: str = "main"
    ):
        """
        Fetch a binary file and return raw bytes.
        Useful for PDFs, images, ZIP files, etc.
        """

        response = self.get_file_content(
            repository_name=repository_name,
            path=path,
            branch=branch
        )

        return base64.b64decode(
            response["content"]
        )