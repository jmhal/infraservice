from pyws.server import SoapServer
from pyws.functions.register import register

server = SoapServer(
        service_name = 'BackEnd',
        tns = 'http://www.mdcc.ufc.br/backend/hpcshelf',
        location = 'http://localhost:8000/backend/',
)

@register(return_type=int, args=str)
def deploy_contract(contract):
    return a + b

@register(return_type=str, args=int)
def platform_deployment_status(platform_id):
    pass

@register(return_type=str, args=int)
def get_platform_endpoint(platform_id):
    pass

@register(return_type=str, args=int)
def destroy_platform(platform_id):
    pass
