import time
import yaml

from os import environ as env

from pyws.server import SoapServer
from pyws.functions.register import register

from common.platform import Platform
from abstraction.infrastructurefactory import InfrastructureFactory

server = SoapServer(
        service_name = 'BackEnd',
        tns = 'http://www.mdcc.ufc.br/hpcshelf/backend/',
        location = 'http://localhost:8000/backend/',
)

# must protect access
# profile_files = "/home/jmhal/repositorios/infraservice/profiles/profiles_cluster_local.yaml"
profiles_file = env['PROFILES_FILE']
infrastructure = InfrastructureFactory(profiles_file).get_infrastructure()

# This is necessary for the web service to be able to return a dictionary.
# It must know beforehand the type.
profiles_ids = {0: 'profiles_ids', 'profile_name': str, 'profile_id': int}
@register(return_type=[profiles_ids])
def available_profiles():
    """
    Returns the available profiles for this backend.
    Input: no need for input
    Output: a dictionary with the profiles.
    """
    global profiles_file
    profiles_available = []
    profiles = yaml.load(open(profiles_file,"r"))['infrastructure']['profiles']
    for profile_name in profiles.keys():
        profiles_available.append({'profile_name': profile_name,
                                   'profile_id': profiles[profile_name]['id']})
    return profiles_available

@register()
def deploy_contract(contract):
    """
    It receives an string containing the contract. This contract is in XML format.
    It will extract the profile ID from the contract and will create the corresponding
    platform.
    Input: An XML string representing the contract
    Output: An ID for the platform to be created. If it can't be created, the value
    will be 0.
    """
    global infrastructure
    profile_id = extract(contract)
    platform_id = infrastructure.create_platform(profile_id)
    return platform_id

@register()
def platform_deployment_status(platform_id):
    """
    The deploy will take time, even in a public cloud. This method returns the
    state of the deployment.
    Input: The ID of the platform.
    Output: Status. This can be BUILDING, FAILED or NULL.
    """
    global infrastructure
    return infrastructure.platform_status(platform_id)


@register()
def get_platform_endpoint(platform_id):
    """
    After the deployment is completed, the endpoints to the platform are made
    available.
    Input: The ID of the platform.
    Output: A string with the endpoint or NULL if nonexistent platform.
    """
    return platform_id

# This is necessary for the web service to be able to return a dictionary.
# It must know beforehand the type.
platforms = {0: 'platforms', 'platform_id': str, 'profile_id': int}
@register(return_type=[platforms])
def available_platforms():
    """
    Lists the platforms currently instantiated.
    Input: there is no need for input.
    Output: A list of platform id's.
    """
    global infrastructure
    platforms_dict = infrastructure.get_available_platforms()
    platform_list = [ {'platform_id': c, 'profile_id': platforms_dict[c]} for c in platforms_dict ]
    return platform_list

@register()
def destroy_platform(platform_id):
    """
    Just destroy the platform.
    Input: The ID of the platform.
    Output: SUCCESS or NULL if nonexistent platform.
    """
    # return infrastructure.destroy_platform(platform_id)
    return platform_id

def extract(contract):
    return int(contract)

def main():
    print profile_files

    platform0_id = deploy_contract(0)
    if platform0_id != 0:
       print "Platform ID: " + str(platform0_id)
       status = "BUILDING"
       while status == "BUILDING":
          print status
          status = platform_deployment_status(platform0_id)
          time.sleep(5)
       print status

    else :
       print "Unable to allocate profile 0"

    platform1_id = deploy_contract(0)
    if platform1_id != 0:
       print "Platform ID: " + str(platform1_id)
       status = "BUILDING"
       while status == "BUILDING":
          print status
          status = platform_deployment_status(platform1_id)
          time.sleep(5)
       print status
    else :
       print "Unable to allocate profile 0"

    destroy_platform(platform0_id)
    destroy_platform(platform1_id)

if __name__ == "__main__":
    main()
