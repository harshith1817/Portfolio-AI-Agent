import json


class ContextFormatter:

    def format(self, contexts):

        formatted = []

        for context in contexts:

            tool = context["tool"].upper()

            formatted.append(f"\n========== {tool} ==========\n\n")

            result = context["result"]

            if isinstance(result, dict):

                formatted.append(
                    json.dumps(
                        result,
                        indent=4,
                        ensure_ascii=False
                    )
                )

            elif isinstance(result, list):

                formatted.append(
                    json.dumps(
                        result,
                        indent=4,
                        ensure_ascii=False
                    )
                )

            else:

                formatted.append(str(result))

            formatted.append("\n")

        return "".join(formatted)