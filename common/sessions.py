from multiprocessing import Lock
from common import Platform

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
