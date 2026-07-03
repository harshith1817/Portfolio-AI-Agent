from abc import ABC, abstractmethod


class BaseTool(ABC):

    @abstractmethod
    def execute(self, action: str, parameters: dict):
        pass