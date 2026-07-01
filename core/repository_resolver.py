from rapidfuzz import process, fuzz


class RepositoryResolver:

    def __init__(self, threshold: int = 70):
        self.threshold = threshold

    def resolve(self, query: str, repositories: list):

        if not repositories:
            raise ValueError("Repository list is empty.")

        repository_names = [
            repo["name"] if isinstance(repo, dict) else repo
            for repo in repositories
        ]

        match = process.extractOne(
            query,
            repository_names,
            scorer=fuzz.WRatio
        )

        if match is None:
            raise ValueError(
                f"No repository found matching '{query}'."
            )

        repository_name, score, _ = match

        if score < self.threshold:
            raise ValueError(
                f"No close repository match found for '{query}'."
            )

        return repository_name