from parsers.portfolio_parser import PortfolioParser
from services.portfolio_service import PortfolioService


class PortfolioTool:

    def __init__(self):

        self.service = PortfolioService()

        self.parser = PortfolioParser()

    def get_portfolio_context(self):

        pages = self.service.get_portfolio_pages()

        return self.parser.parse(pages)