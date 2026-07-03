import base64

from clients.github_client import GitHubClient
from parsers.github_readme_parser import GitHubReadmeParser
from parsers.portfolio_parser import PortfolioParser
from core.config import GITHUB_PORTFOLIO_REPOSITORY
from core.repository_resolver import RepositoryResolver
from parsers.github_profile_parser import GitHubProfileParser


class GitHubService:

    PORTFOLIO_REPOSITORY = GITHUB_PORTFOLIO_REPOSITORY

    PORTFOLIO_FILES = {
        "projects": "Frontend/src/pages/Projects/index.jsx",
        "about": "Frontend/src/pages/About/index.jsx",
        "skills": "Frontend/src/pages/About/index.jsx",
        "certifications": "Frontend/src/pages/Certifications/index.jsx",
        "achievements": "Frontend/src/pages/Certifications/index.jsx",
        "contact": "Frontend/src/Footer.jsx"
    }

    def __init__(self):
        self.client = GitHubClient()

        self.readme_parser = GitHubReadmeParser()
        self.profile_parser = GitHubProfileParser()
        self.portfolio_parser = PortfolioParser()

        self.repository_resolver = RepositoryResolver()

        self._portfolio_cache = {}
        self._project_cache = {}
        self._profile_cache = None
        self._repositories_cache = None
        
    def get_repositories(self):

        if self._repositories_cache is not None:
            return self._repositories_cache

        repositories = self.client.get_repositories()

        self._repositories_cache = [
            {
                "name": repo.get("name"),
                "description": repo.get("description"),
                "language": repo.get("language"),
                "url": repo.get("html_url")
            }
            for repo in repositories
        ]

        return self._repositories_cache

    def get_repository(self, repository_name: str):
        return self.client.get_repository(repository_name)

    def get_languages(self, repository_name: str):
        return self.client.get_languages(repository_name)

    def get_readme(self, repository_name: str):

        response = self.client.get_readme(repository_name)

        content = base64.b64decode(
            response["content"]
        ).decode("utf-8")

        return self.readme_parser.parse(content)

    def get_portfolio_file(self, section: str):

        if section in self._portfolio_cache:
            return self._portfolio_cache[section]

        path = self.PORTFOLIO_FILES[section]

        jsx = self.client.get_file_text(
            repository_name=self.PORTFOLIO_REPOSITORY,
            path=path
        )

        parsed = self.portfolio_parser.parse(
            section=section,
            jsx=jsx
        )

        self._portfolio_cache[section] = parsed

        return parsed

    def get_project(self, repository_name: str):

        repositories = self.get_repositories()

        repository_name = self.repository_resolver.resolve(
            repository_name,
            repositories
        )

        if repository_name in self._project_cache:
            return self._project_cache[repository_name]

        repository = self.get_repository(repository_name)
        readme = self.get_readme(repository_name)
        languages = self.get_languages(repository_name)

        project = {
            "name": repository["name"],
            "description": repository["description"],
            "primary_language": repository["language"],
            "languages": languages,
            "url": repository["html_url"],
            "updated_at": repository["updated_at"],
            "topics": repository.get("topics", []),
            "readme": readme
        }

        self._project_cache[repository_name] = project

        return project
        
    def get_profile(self):

        if self._profile_cache is not None:
            return self._profile_cache

        response = self.client.get_readme("harshith1817")

        content = base64.b64decode(
            response["content"]
        ).decode("utf-8")

        parsed = self.profile_parser.parse(content)

        self._profile_cache = parsed

        return parsed