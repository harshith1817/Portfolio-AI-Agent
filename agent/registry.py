from tools.github_tool import GitHubTool
from tools.resume_tool import ResumeTool
from tools.portfolio_tool import PortfolioTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "github": GitHubTool(),
            "resume": ResumeTool(),
            "portfolio": PortfolioTool()
        }

    def get_tool(self, name: str):

        return self.tools.get(name)