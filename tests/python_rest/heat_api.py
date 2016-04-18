#!/home/jmhal/heatclient/bin/python
# https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html
import json
import requests
import os
import yaml

from os import environ as env
from os import path as path

from heatclient.common import template_utils

def get_auth_token(url, tenant, username, password):
   headers = {'Content-Type':'application/json'}
   payload = {'auth':{'tenantName': tenant, 'passwordCredentials':{ 'username': username, 'password': password}}}
   r = requests.post(url, data = json.dumps(payload), headers = headers)
   token_id = r.json()['access']['token']['id']
   return token_id

def get_tenant_id(url, token, tenant):
   headers = {'X-Auth-Token': token}
   r = requests.get(url, headers=headers)
   json = r.json()
   for element in json['tenants']:
      if element['name'] == tenant:
          return element['id']

def get_fields(tenant_id, stack_name, template_file, params):
    tpl_files, template = template_utils.get_template_contents(template_file = template_file)
    fields = {
        'tenant_id' : tenant_id,
        'stack_name': stack_name,
        'parameters': params,
        'template': template,
        'files': dict(list(tpl_files.items())),
    }
    return fields

def create_stack(token, tenant_id, heat_base_url, stack_name, template_file, params):
    headers = {'X-Auth-Token': token}
    fields = get_fields(tenant_id, stack_name, template_file, params)
    r = requests.post(heat_base_url + "/" + tenant_id + "/stacks", data = json.dumps(fields), headers = headers)
    print r.status_code
    print r.text
    data = r.json()
    print data['stack']['id']
    return data['stack']['id']

username = env['OS_USERNAME']
password = env['OS_PASSWORD']
tenant_name = env['OS_TENANT_NAME']
token = get_auth_token(env['OS_AUTH_URL'] + "/tokens", tenant_name, username, password)
tenant_id = get_tenant_id(env['OS_AUTH_URL'] + "/tenants", token, tenant_name)
heat_base_url = "http://" + env['OS_AUTH_URL'].split(":")[1][2:] + ":8004/v1"

params = {}
params['image'] = 'Ubuntu1404'
params['flavor'] = 'shelf.medium'
params['key'] = 'joaoalencar'
params['public_network'] = 'ext-net'
params['cluster_size'] = '4'

template_file = "/home/jmhal/repositorios/infraservice/tests/heat_templates/cluster.yaml"

create_stack(token = token, tenant_id = tenant_id, heat_base_url = heat_base_url,
             stack_name="teste", template_file = template_file, params=params)
