from pyws.server import SoapServer
from pyws.functions.register import register
from common.platform import Platform

server = SoapServer(
        service_name = 'BackEnd',
        tns = 'http://www.mdcc.ufc.br/hpcshelf/backend/',
        location = 'http://localhost:8000/backend/',
)

# must protect access
infrastructure = InfrastructureFactory(profile_files).get_infrastructure()

@register(return_type=str, args=[str])
def deploy_contract(contract):
    """
    It receives an string containing the contract. This contract is in XML format.
    It will extract the profile ID from the contract and will create the corresponding
    platform.
    Input: An XML string representing the contract
    Output: An ID for the platform to be created.
    """
    global infrastructure
    profile_id = extract(contract)
    platform_id = infrastructure.create_platform(profile_id)
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
