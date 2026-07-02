import json


class ProfileService:

    def __init__(self):

        with open(
            "data/profile.json",
            encoding="utf-8"
        ) as f:

            self.profile = json.load(f)

    def get_profile(self):
        return self.profile