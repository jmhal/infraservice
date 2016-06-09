class ProfileNotFound(Exception):
    def __init__(self, profile_id, profiles):
        self.profile_id = profile_id
        self.profiles = profiles
    def __str__(self):
        return "ID " + str(self.profile_id) + " not found in " + str(self.profiles)

class ResourcesNotAvailable(Exception):
    def __init__(self, profile_id, required_resources):
        self.profile_id = profile_id
        self.required_resources = required_resources
    def __str__(self):
        return "Profile ID: " + str(self.profile_id) + " Resources Not Available: " + self.required_resources

class PlatformDoesNotExist(Exception):
    def __init__(self, platform_id):
        self.platform_id = platform_id
    def __str__(self):
        return "There is no platform with ID: " + str(self.platform_id)
