# must use django-admin startproject webservices
from pyws.server import SoapServer
from pyws.functions.register import register
from pyws.functions import Function

server = SoapServer(
        service_name = 'Test',
        tns = 'http://example.com',
        location = 'http://localhost:8000/api/',
)

@register()
def add_simple(a, b):
   return a + b
