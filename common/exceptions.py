from exceptions import Exception
class ProfileNotFound(Exception):
    def __init__(self, profile_id, profiles):
        self.profile_id = profile_id
        self.profiles = profiles
    def __str__(self):
        return "ID " + str(self.profile_id) + " not found in " + str(self.profiles)
