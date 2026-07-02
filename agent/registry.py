from tools.github_tool import GitHubTool
from tools.resume_tool import ResumeTool
from tools.portfolio_tool import PortfolioTool
from tools.profile_tool import ProfileTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "github": GitHubTool(),
            "resume": ResumeTool(),
            "portfolio": PortfolioTool(),
            "profile": ProfileTool()
        }

    def get_tool(self, name: str):

        return self.tools.get(name)