from pyws.server import SoapServer
from pyws.functions.register import register

server = SoapServer(
        service_name = 'BackEnd',
        tns = 'http://www.mdcc.ufc.br/backend/hpcshelf',
        location = 'http://localhost:8000/backend/',
)

class PlatformDeployment:
    def __init__(self, infrastructure, id, endpoint, status):
        self.infrastructure = infrastructure
        self.id = id
        self.endpoint = endpoint
        self.status = status
    def get_infrastructure(self):
        return self.infrastructure
    def update_status(self, status):
        self.status = status
    def get_status(self):
        return self.status
    def get_id(self):
        return self.id
    def get_endpoint(self):
        return self.endpoint

class Deployments:
    def __init__(self):
        self.deployments = []
    def get_platforms(self):
        return self.deployments
    def add_platform(self, platform):
        self.deployments.append(platform)
    def remove_platform(self, platform):
        temp = PlatformDeployment(-1, "","")
        for x in self.deployments:
            if x.get_id() == platform.get_id():
                temp = x
        try:
            self.deployments.remove(temp)
            return 0
        except ValueError:
            return 1
    def persist_platforms(self):
        pass
    def load_platforms(self):
        pass

platforms = Deployments();

@register(return_type=int, args=[str])
def deploy_contract(contract):
    """
    It receives an string containing the contract. This contract is in XML format.
    It will extract the profile ID from the contract and will create the corresponding
    platform.
    Input: An XML string representing the contract
    Output: An ID for the platform to be created.
    """
    global platforms
    profileID = extract(contract)
    platform = infrastructure.create_profile(profileID)
    platform_id = create_unique_identifier()
    platforms.add_platform(PlatformDeployment(platform, platform_id, "", "BUILDING"))
    return platform_id

@register(return_type=str, args=[int])
def platform_deployment_status(platform_id):
    """
    The deploy will take time, even in a public cloud. This method returns the
    state of the deployment.
    Input: The ID of the platform.
    Output: Status. This can be BUILDING, FAILED or NULL.
    """
    pass

@register(return_type=str, args=[int])
def get_platform_endpoint(platform_id):
    """
    After the deployment is completed, the endpoints to the platform are made
    available.
    Input: The ID of the platform.
    Output: A string with the endpoint or NULL if nonexistent platform.
    """
    pass

@register(return_type=str, args=[int])
def destroy_platform(platform_id):
    """
    Just destroy the platform.
    Input: The ID of the platform.
    Output: SUCCESS or NULL if nonexistent platform.
    """
    pass
