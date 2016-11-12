import suds
client = suds.client.Client('http://192.168.1.110:8000/api/wsdl', cache=None)
a = client.service.add_simple('hello ', 'world')
print a
