from agent.registry import ToolRegistry


class Executor:

    def __init__(self):

        self.registry = ToolRegistry()

    def execute(self, plan: dict):

        contexts = []

        for step in plan["plan"]:

            tool = self.registry.get_tool(step["tool"])

            if tool is None:
                continue

            result = tool.execute(
                action=step["action"],
                parameters=step.get("parameters", {})
            )

            contexts.append({
                "tool": step["tool"],
                "action": step["action"],
                "result": result
            })

        return contexts