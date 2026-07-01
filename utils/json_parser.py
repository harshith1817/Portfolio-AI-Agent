import json


class JSONParser:

    @staticmethod
    def parse(response: str):

        response = response.strip()

        if response.startswith("```json"):
            response = response[len("```json"):]

        elif response.startswith("```"):
            response = response[3:]

        if response.endswith("```"):
            response = response[:-3]

        try:
            return json.loads(response)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Invalid JSON returned by LLM:\n\n{response}"
            ) from e