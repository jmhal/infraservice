from multiprocessing import Lock

class Platform:
    def __init__(self, id, endpoint, status):
        self.id = id
        self.endpoint = endpoint
        self.status = status

    def update_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_id(self):
        return self.id

    def get_endpoint(self):
        return self.endpoint

class Sessions:
    """
    This class with hold the current allocations and platforms. 
    """
    def __init__(self):
        self.sessions = []
        self.mutex = Lock()

    def add_platform(self, platform):
        with self.mutex:
           self.sessions.append(platform)

    def get_platform(self, platform_id):
        with self.mutex:
           for p in self.sessions:
              if p.id = platform_id:
                 return p

    def remove_platform(self, platform_id):
        with self.mutex:
           self.sessions = [ p for p in self.sessions if p.get_id() != platform_id]

    def update_platform(self, platform):
        self.remove_platform(platform.get_id())
        self.add_platform(platform)
