# must use django-admin startproject webservices
from pyws.server import SoapServer
from pyws.functions.register import register
from pyws.functions import Function

from pyws.functions import NativeFunctionAdapter
from pyws.functions.args import String, DictOf, Field, TypeFactory

from inspect import getargspec

server = SoapServer(
        service_name = 'Test',
        tns = 'http://example.com',
#        location = 'http://localhost:8000/api/',
        location = 'http://192.168.1.110:8000/api/',
)

@register()
def add_triple(a, b, c):
   return a + b + c

class Add_Simple(Function):
   def __init__(self):
      self.remote_ip = None
      self.name = "add_simple"
      self.documentation = "a simple add/concatenate function"
      self.return_type = TypeFactory(str)
      self.needs_context = False 
      args_ = [('a', str), ('b', str)]
      self.args = DictOf("add_simple", *args_)

   def call(self, **args):
      return self.add_simple(**args)

   def add_simple(self, a, b):
      print "The remote IP is", self.remote_ip
      return a + b

f  = Add_Simple()
server.add_function(f)

