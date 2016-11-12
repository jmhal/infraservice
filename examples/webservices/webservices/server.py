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
        location = 'http://localhost:8000/api/',
#        location = 'http://192.168.1.110:8000/api',
)

"""
@register('add_simple',needs_context=True)
def add_simple(a, b, context):
   print "The Remote IP is", context
   return a + b


f = NativeFunctionAdapter(add_simple)
server.add_function(f)
"""

class Add_Simple(Function):
   def __init__(self):
      self.remote_ip = None
      self.name = "add_simple"
      self.documentation = "who cares?"
      self.return_type = TypeFactory(str)
      self.needs_context = False 
      args_ = [('a', str), ('b', str)]
      self.args = DictOf("add_simple", *args_)

   def call(self, **args):
      print args
      return self.add_simple(**args)

   def add_simple(self, a, b):
      print "The remote IP is", self.remote_ip
      return a + b

f  = Add_Simple()

# print len(f.args.fields)
# field0 = f.args.fields[0]
# print field0.name
# print field0.type
# print f.return_type

server.add_function(f)

