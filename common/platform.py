class Platform:
    def __init__(self, id, resources_id, endpoint, status):
        self.id = id
        self.resource_id = resources_id
        self.endpoint = endpoint
        self.status = status

    def get_id(self):
        return self.id

    def get_resources_id(self):
        return self.resources_id

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_endpoint(self):
        self.endpoint = endpoint

    def get_endpoint(self):
        return self.endpoint
