from tools.resume_tool import ResumeTool
from tools.portfolio_tool import PortfolioTool
from tools.github_tool import GitHubTool


class AgentRouter:

    def __init__(self):

        self.resume_tool = ResumeTool()
        self.portfolio_tool = PortfolioTool()
        self.github_tool = GitHubTool()
        
    def route(self, query: str):

        query = query.lower()

        if any(word in query for word in [
            "project",
            "repository",
            "github",
            "repo",
            "commit"
        ]):
            return ["github"]

        elif any(word in query for word in [
            "skill",
            "education",
            "resume",
            "experience"
        ]):
            return ["resume"]

        elif any(word in query for word in [
            "certificate",
            "certification",
            "achievement",
            "contact"
        ]):
            return ["portfolio"]

        else:
            return []