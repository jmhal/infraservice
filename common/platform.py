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
