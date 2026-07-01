import re


class GitHubReadmeParser:

    def parse(self, readme: str):

        readme = self._clean(readme)

        return {
            "overview": self._extract_section(
                readme,
                "Overview"
            ),
            "features": self._extract_bullets(
                readme,
                "Features"
            ),
            "technologies": self._extract_bullets(
                readme,
                "Technologies Used"
            ),
            "deployment": self._extract_bullets(
                readme,
                "Live Demos"
            )
        }
        
    def _clean(self, text):

        text = re.sub(
            r'!\[.*?\]\(.*?\)',
            '',
            text
        )

        text = re.sub(
            r'<img.*?>',
            '',
            text
        )

        text = re.sub(
            r'\n{3,}',
            '\n\n',
            text
        )

        return text.strip()
    
    
    def _extract_section(self, text, heading):

        pattern = rf"## .*{heading}(.*?)(## |\Z)"

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if not match:
            return ""

        return match.group(1).strip()
    
    def _extract_bullets(self, text, heading):

        section = self._extract_section(
            text,
            heading
        )

        bullets = []

        for line in section.splitlines():

            line = line.strip()

            if line.startswith("-"):
                bullets.append(
                    line[1:].strip()
                )

        return bullets