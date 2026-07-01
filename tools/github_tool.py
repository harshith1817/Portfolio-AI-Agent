from services.github_service import GitHubService


class GitHubTool:

    def __init__(self):
        self.service = GitHubService()

    def execute(self, action: str, parameters: dict):

        if action == "project":
            return self.service.get_project(
                parameters["repository"]
            )

        elif action == "repository":
            return self.service.get_repository(
                parameters["repository"]
            )

        elif action == "repositories":
            return self.service.get_repositories()

        elif action == "languages":
            return self.service.get_languages(
                parameters["repository"]
            )

        elif action == "readme":
            return self.service.get_readme(
                parameters["repository"]
            )

        elif action == "portfolio_file":
            return self.service.get_portfolio_file(
                parameters["section"]
            )

        elif action == "profile":
            return self.service.get_profile()

        raise ValueError(
            f"Unsupported GitHub action: {action}"
        )