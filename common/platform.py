class Platform:
    def __init__(self, id, profile_id, allocation_id, endpoint, status):
        self.id = id
        self.profile_id = profile_id
        self.allocation_id = allocation_id
        self.endpoint = endpoint
        self.status = status

    def __str__(self):
        return "ID: " + str(self.id) + " Allocation ID: " + str(self.allocation_id) + " Endpoint: " + self.endpoint + " Status: " + self.status

    def get_id(self):
        return self.id

    def get_profile_id(self):
        return self.profile_id

    def get_allocation_id(self):
        return self.allocation_id

    def set_allocation_id(self, allocation_id):
        self.allocation_id = allocation_id

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def get_endpoint(self):
        return self.endpoint
