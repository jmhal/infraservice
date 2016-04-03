#!/usr/bin/python

import json
import requests
import os

from os import environ as env
from os import path as path
from datetime import datetime
from dateutil import parser as parser
from pytz import UTC as utc

def get_auth_token(url, tenant, username, password):
   if path.isfile("token.tmp"):
      token_file = open("token.tmp", "r+")
      expiration_date = parser.parse(token_file.readline().strip())
      present = utc.localize(datetime.now())
      if present < expiration_date:
         token_id = token_file.readline().strip()
         token_file.close()
         return token_id
      else:
         token_file.close()
         os.remove("token.tmp")
   headers = {'Content-Type':'application/json'}
   payload = {'auth':{'tenantName': tenant, 'passwordCredentials':{ 'username': username, 'password': password}}}
   r = requests.post(url, data = json.dumps(payload), headers = headers)
   token_expires = r.json()['access']['token']['expires']
   token_id = r.json()['access']['token']['id']
   token_file = open("token.tmp", "w+")
   token_file.write(token_expires + '\n')
   token_file.write(token_id + '\n')
   token_file.close()
   return token_id

def get_tenant_id(url, token, tenant):
   headers = {'X-Auth-Token': token}
   r = requests.get(url, headers=headers)
   json = r.json()
   for element in json['tenants']:
      if element['name'] == tenant:
          return element['id']

def list_flavors(url, token):
   headers = {'X-Auth-Token': token}
   r = requests.get(url, headers=headers)
   json = r.json()
   for element in json['flavors']:
      print element['name']


def list_stacks(url, token, tenant_id):
   headers = {'X-Auth-Token': token, 'tenant_id': tenant_id}
   r = requests.get(url, headers=headers)
   json = r.json()
   for element in json['stacks']:
      print element['stack_name']        

auth_url = env['OS_AUTH_URL'] + "/tokens"
#base_url = url.split(":")[1][2:]
#urls = {"nova": "http://" + base_url + ":8774/v2/", "identity": "http://" + base_url + ":5000/v2/"

username = env['OS_USERNAME'] 
password = env['OS_PASSWORD']
tenant_name = env['OS_TENANT_NAME']
token = get_auth_token(auth_url, tenant_name, username, password)
tenant_id = get_tenant_id(env['OS_AUTH_URL'] + "/tenants", token, tenant_name)
list_stacks("http://200.19.177.89:8004/v1/" + tenant_id + "/stacks", token, tenant_id)

#list_flavors("http://200.19.177.89:8774/v2/" + 
#              get_tenant_id(env['OS_AUTH_URL'] + "/tenants", token, tenant_name) 
#              + "/flavors", 
#              get_auth_token(auth_url, tenant_name, username, password))
