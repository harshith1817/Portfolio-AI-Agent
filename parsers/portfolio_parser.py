import re


class PortfolioParser:

    def parse(self, section: str, jsx: str):

        if section == "projects":
            return self.extract_projects(jsx)

        elif section == "certifications":
            return self.extract_certifications(jsx)
        
        elif section == "achievements":
            return self.extract_achievements(jsx)
        
        elif section == "about":
            return self.extract_about(jsx)

        elif section == "contact":
            return self.extract_contact(jsx)

        raise ValueError(
            f"Unknown portfolio section: {section}"
        )

    def extract_projects(self, jsx: str):

        projects = []

        project_blocks = re.findall(
            r"<ProjectContainer>(.*?)</ProjectContainer>",
            jsx,
            re.DOTALL
        )

        for block in project_blocks:

            name = self.extract(
                r"<ProjectHeading>(.*?)</ProjectHeading>",
                block
            )

            description = self.extract(
                r"<ProjectDesc>(.*?)</ProjectDesc>",
                block
            )

            links = re.findall(
                r'href="([^"]+)"',
                block
            )

            project = {
                "name": "",
                "description": "",
                "github": "",
                "demo": ""
            }

            project["name"] = name
            project["description"] = description

            if len(links) >= 1:
                project["github"] = links[0]

            if len(links) >= 2:
                project["demo"] = links[1]

            projects.append(project)

        return {
            "projects": projects
        }

    def extract_certifications(self, jsx: str):

        certifications = []

        certificate_blocks = re.findall(
            r"<CertificateContainer>(.*?)</CertificateContainer>",
            jsx,
            re.DOTALL
        )

        for block in certificate_blocks:

            title = self.extract(
                r"<CertificationTitle>.*?/>?(.*?)</CertificationTitle>",
                block
            )

            organization = self.extract(
                r"<CertificationOrganization>(.*?)</CertificationOrganization>",
                block
            )

            description = self.extract(
                r"<CertificationDescription>(.*?)</CertificationDescription>",
                block
            )

            skills = [
                self.clean_text(skill)
                for skill in re.findall(
                    r"<Skills>(.*?)</Skills>",
                    block,
                    re.DOTALL
                )
            ]

            credential = self.extract_url(
                r'href="([^"]+)"',
                block
            )

            certifications.append(
                {
                    "title": title,
                    "organization": organization,
                    "description": description,
                    "skills": skills,
                    "credential": credential
                }
            )

        return {
            "certifications": certifications
        }

    def extract_achievements(self, jsx: str):

        achievements = []

        achievement_blocks = re.findall(
            r"<AchievementContainer.*?>(.*?)</AchievementContainer>",
            jsx,
            re.DOTALL
        )

        for block in achievement_blocks:

            badge = self.extract(
                r"<BadgeSpan>(.*?)</BadgeSpan>",
                block
            )

            title = self.extract(
                r"<h3.*?>(.*?)</h3>",
                block
            )

            description = self.extract(
                r"<AcheivementDescription>(.*?)</AcheivementDescription>",
                block
            )

            url = self.extract_url(
                r'window\.open\(\s*"([^"]+)"',
                block
            )

            achievements.append(
                {
                    "title": title,
                    "badge": badge,
                    "description": description,
                    "url": url
                }
            )

        return {
            "achievements": achievements
        }
        
    def extract_about(self, jsx: str):

        bio = []

        bio_matches = re.findall(
            r"<Bio2?>(.*?)</Bio2?>",
            jsx,
            re.DOTALL
        )

        for paragraph in bio_matches:

            # Remove <Diff> tags while keeping the text
            paragraph = re.sub(
                r"</?Diff>",
                "",
                paragraph
            )

            # Remove any remaining JSX tags
            paragraph = re.sub(
                r"<.*?>",
                "",
                paragraph
            )

            # Normalize whitespace
            paragraph = " ".join(
                paragraph.split()
            )

            if paragraph:
                bio.append(paragraph)

        return {
            "bio": bio
        }
        
    def extract_url(self, pattern: str, text: str) -> str:

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        return match.group(1) if match else ""

    def extract_contact(self, jsx: str):

        patterns = {
            "github": r'https://github\.com/[^"\']+',
            "linkedin": r'https://www\.linkedin\.com/[^"\']+',
            "email": r'mailto:([^"\']+)',
            "instagram": r'https://www\.instagram\.com/[^"\']+',
            "twitter": r'https://www\.x\.com/[^"\']+'
        }

        contacts = {}

        for key, pattern in patterns.items():

            match = re.search(pattern, jsx)

            if match:

                contacts[key] = match.group(1) if key == "email" else match.group(0)

        return contacts
    
    def clean_text(self, text: str) -> str:

        if not text:
            return ""

        text = re.sub(r"</?Diff>", "", text)
        text = re.sub(r"<.*?>", "", text)

        return " ".join(text.split())
    
    def extract(self, pattern: str, text: str) -> str:

        match = re.search(
            pattern,
            text,
            re.DOTALL
        )

        if not match:
            return ""

        return self.clean_text(match.group(1))