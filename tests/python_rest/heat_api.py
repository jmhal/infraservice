#!/usr/bin/python
# http://developer.openstack.org/api-guide/quick-start/api-quick-start.html
from os import environ as env
import keystoneclient.v2_0.client as ksclient
from heatclient.client import Client

keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           tenant_name=env['OS_TENANT_NAME'],
                           region_name=env['OS_REGION_NAME'])

heat_url = 'http://200.19.177.89:8004/v1/%s' % keystone.tenant_id
heat = Client('1', endpoint=heat_url, token=keystone.auth_token)

# keystone.tenant_id
# stack_name = "api_cluster"
# template_url = "https://raw.githubusercontent.com/jmhal/infraservice/master/tests/heat_templates/heat_2a.yaml"
parameters = "{'parameters':{ 'image' : 'Ubuntu1404', 'flavor' : 'hpcshelf.medium', 'key':'joaoalencar', 'private_network' : 'demonet'}}"


fields = {
	    'tenant_id' : keystone.tenant_id,
            'stack_name': 'api_teste',
            'parameters': parameters,
            'template_url': 'https://raw.githubusercontent.com/jmhal/infraservice/master/tests/heat_templates/heat_2a.yaml'
        }	
heat.stacks.create(**fields)
