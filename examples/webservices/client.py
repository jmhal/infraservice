import suds
client = suds.client.Client('http://localhost:8000/api/wsdl', cache=None)
a = client.service.add_simple('hello ', 'world')
print a
