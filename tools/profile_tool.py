from services.profile_service import ProfileService


class ProfileTool:

    def __init__(self):
        self.service = ProfileService()

    def execute(self, action: str, parameters: dict):

        if action == "profile":
            return self.service.get_profile()

        raise ValueError(f"Unsupported Profile action: {action}")