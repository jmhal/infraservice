import suds
client = suds.client.Client('http://localhost:8000/api/wsdl', cache=None)
client.service.add_simple('hello ', 'world')
