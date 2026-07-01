import re


class PortfolioParser:

    def parse(self, section: str, jsx: str):

        if section == "projects":
            return self.extract_projects(jsx)

        elif section == "certifications":
            return self.extract_certifications(jsx)
        
        elif section == "achievements":
            return self.extract_certifications(jsx)
        
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

            name_match = re.search(
                r"<ProjectHeading>(.*?)</ProjectHeading>",
                block,
                re.DOTALL
            )

            description_match = re.search(
                r"<ProjectDesc>(.*?)</ProjectDesc>",
                block,
                re.DOTALL
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

            if name_match:
                project["name"] = " ".join(
                    name_match.group(1).split()
                )

            if description_match:
                project["description"] = " ".join(
                    description_match.group(1).split()
                )

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

            title = re.search(
                r"<CertificationTitle>.*?/>?(.*?)</CertificationTitle>",
                block,
                re.DOTALL
            )

            organization = re.search(
                r"<CertificationOrganization>(.*?)</CertificationOrganization>",
                block,
                re.DOTALL
            )

            description = re.search(
                r"<CertificationDescription>(.*?)</CertificationDescription>",
                block,
                re.DOTALL
            )

            skills = re.findall(
                r"<Skills>(.*?)</Skills>",
                block
            )

            credential = re.search(
                r'href="([^"]+)"',
                block
            )

            certifications.append(
                {
                    "title": " ".join(title.group(1).split()) if title else "",
                    "organization": " ".join(organization.group(1).split()) if organization else "",
                    "description": " ".join(description.group(1).split()) if description else "",
                    "skills": [skill.strip() for skill in skills],
                    "credential": credential.group(1) if credential else ""
                }
            )

        achievements = []

        achievement_blocks = re.findall(
            r"<AchievementContainer.*?>(.*?)</AchievementContainer>",
            jsx,
            re.DOTALL
        )

        for block in achievement_blocks:

            badge = re.search(
                r"<BadgeSpan>(.*?)</BadgeSpan>",
                block,
                re.DOTALL
            )

            title = re.search(
                r"<h3.*?>(.*?)</h3>",
                block,
                re.DOTALL
            )

            description = re.search(
                r"<AcheivementDescription>(.*?)</AcheivementDescription>",
                block,
                re.DOTALL
            )

            link = re.search(
                r'window\.open\(\s*"([^"]+)"',
                block,
                re.DOTALL
            )

            achievements.append(
                {
                    "title": " ".join(title.group(1).split()) if title else "",
                    "badge": " ".join(badge.group(1).split()) if badge else "",
                    "description": " ".join(description.group(1).split()) if description else "",
                    "url": link.group(1) if link else ""
                }
            )

        return {
            "certifications": certifications,
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

    def extract_contact(self, jsx: str):

        contacts = {}

        github = re.search(
            r'https://github\.com/[^"\']+',
            jsx
        )

        linkedin = re.search(
            r'https://www\.linkedin\.com/[^"\']+',
            jsx
        )

        email = re.search(
            r'mailto:([^"\']+)',
            jsx
        )

        instagram = re.search(
            r'https://www\.instagram\.com/[^"\']+',
            jsx
        )

        twitter = re.search(
            r'https://www\.x\.com/[^"\']+',
            jsx
        )

        if github:
            contacts["github"] = github.group(0)

        if linkedin:
            contacts["linkedin"] = linkedin.group(0)

        if email:
            contacts["email"] = email.group(1)

        if instagram:
            contacts["instagram"] = instagram.group(0)

        if twitter:
            contacts["twitter"] = twitter.group(0)

        return contacts