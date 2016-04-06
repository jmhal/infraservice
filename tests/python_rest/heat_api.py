#!/usr/bin/python
# https://docs.saltstack.com/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html
import json
import requests
import os
import yaml

from os import environ as env
from os import path as path
from datetime import datetime
from dateutil import parser as parser
from pytz import UTC as utc

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

def create_stack(url, token, tenant_id, stack_name, template_url):
    headers = {'X-Auth-Token': token}
    payload = {'tenant_id' : tenant_id, 'stack_name' : stack_name, 'template_url' : template_url,
               'parameters' : {'image' : 'Ubuntu1404', 'flavor' : 'shelf.medium',
               'key' : 'joaoalencar', 'private_network' : 'demo-net'}}
    r = requests.post(url, data = json.dumps(payload), headers = headers)
    print r.text
    data = r.json()
    return data['stack']['id']

def create_stack(url, token, tenant_id, stack_name, template_file, files):
    f = open(template_file, 'r')
    template = yaml.load(f)
    f.close()
    headers = {'X-Auth-Token': token}
    payload = {'tenant_id' : tenant_id, 'stack_name' : stack_name,
               'template' : json.dumps(template),
               'files' : '',
               'parameters' : {'image' : 'Ubuntu1404', 'flavor' : 'shelf.medium',
               'key' : 'joaoalencar', 'private_network' : 'demo-net'}}
    r = requests.post(url, data = json.dumps(payload), headers = headers)
    print r.status_code
    print r.text
    data = r.json()
    return data['stack']['id']

username = env['OS_USERNAME']
password = env['OS_PASSWORD']
tenant_name = env['OS_TENANT_NAME']

token = get_auth_token(env['OS_AUTH_URL'] + "/tokens", tenant_name, username, password)
tenant_id = get_tenant_id(env['OS_AUTH_URL'] + "/tenants", token, tenant_name)

base_url = env['OS_AUTH_URL'].split(":")[1][2:]
heat_base_url = "http://" + base_url + ":8004/v1"

# template_url = "https://raw.githubusercontent.com/jmhal/infraservice/master/tests/heat_templates/heat_2a.yaml"
# create_stack(heat_base_url + "/" + tenant_id + "/stacks", token, tenant_id, "teste_api", template_url=template_url)
template_file = "/home/jmhal/repositorios/infraservice/tests/heat_templates/heat_2a.yaml"
files = {''}
create_stack(heat_base_url + "/" + tenant_id + "/stacks", token, tenant_id, "teste_api_do_arquivo", template_file=template_file)
