#!/home/jmhal/heatclient/bin/python
# https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html
import json
import requests
import os
import yaml
import time

from os import environ as env
from os import path as path

from heatclient.common import template_utils

def get_auth_token(url, tenant_name, username, password):
   headers = {'Content-Type':'application/json'}
   fields = {
       'auth':{
           'tenantName': tenant_name,
           'passwordCredentials':{
               'username': username,
               'password': password}
            }
   }
   r = requests.post(url, data = json.dumps(fields), headers = headers)
   token_id = r.json()['access']['token']['id']
   return token_id

def get_tenant_id(url, token, tenant):
   headers = {'X-Auth-Token': token}
   r = requests.get(url, headers=headers)
   json = r.json()
   for element in json['tenants']:
      if element['name'] == tenant:
          return element['id']

def delete_stack(token, tenant_id, heat_base_url, stack_name, stack_id):
    headers = {'X-Auth-Token': token}
    r = requests.delete(heat_base_url + "/" + tenant_id + "/stacks/" + stack_name + "/" + stack_id, headers = headers)
    return r.status_code

def status_stack(token, tenant_id, heat_base_url, stack_name, stack_id):
    headers = {'X-Auth-Token': token}
    r = requests.get(heat_base_url + "/" + tenant_id + "/stacks/" + stack_name + "/" + stack_id, headers = headers)
    return r.json()

def create_stack(token, tenant_id, heat_base_url, stack_name, template_file, params):
    headers = {'X-Auth-Token': token}
    tpl_files, template = template_utils.get_template_contents(template_file = template_file)
    fields = {
        'tenant_id' : tenant_id,
        'stack_name': stack_name,
        'parameters': params,
        'template': template,
        'files': dict(list(tpl_files.items())),
    }
    r = requests.post(heat_base_url + "/" + tenant_id + "/stacks", data = json.dumps(fields), headers = headers)
    data = r.json()
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

stack_id = create_stack(token = token, tenant_id = tenant_id, heat_base_url = heat_base_url,
             stack_name="teste", template_file = template_file, params=params)

status = status_stack(token = token, tenant_id = tenant_id, heat_base_url = heat_base_url,
             stack_name = "teste", stack_id = stack_id)

while status['stack']['stack_status'] == "CREATE_IN_PROGRESS":
    print "Creating stack..."
    time.sleep(5)
    status = status_stack(token = token, tenant_id = tenant_id, heat_base_url = heat_base_url,
                 stack_name = "teste", stack_id = stack_id)

print "You can access the cluster in: " + status['stack']['outputs'][0]['output_value']


#delete_stack(token = token, tenant_id = tenant_id , heat_base_url = heat_base_url ,
#              stack_name = "teste", stack_id = "4cdf1499-e4b4-4d3b-8174-a61eb4aaac83")
