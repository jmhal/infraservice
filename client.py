import suds
client = suds.client.Client('http://localhost:8000/backend/wsdl', cache=None)

platform_id = client.service.deploy_contract("0")
print platform_id

platform_status = client.service.platform_deployment_status(platform_id)
print platform_status

platform_endpoint = client.service.get_platform_endpoint(platform_id)
print platform_endpoint

platform_destroy_status = client.service.destroy_platform(platform_id)
print platform_destroy_status
