import json
import requests
import os
import yaml
import time

from os import environ as env
from os import path as path
from heatclient.common import template_utils
from infrastructureimplementor import InfrastructureImplementor

class OpenStack(InfrastructureImplementor):
    def __init__(self, properties):
        """
        This will read the rc file and store the value from the environment
        variables to be used at each heat API call.
        """
        self.username = properties['username']
        self.password = properties['password']
        self.key = properties['key']
        self.auth_url = properties['auth_url']
        self.tenant_name = properties['tenant_name']
        self.region_name = properties['region_name']

    def authenticate(self):
        """
        Create a token for the heat API calls.
        """
        self.token = get_auth_token(self.auth_url + "/tokens", self.tenant_name, self.username, self.password)
        return self.token

    def verify_profile_availability(self, profile):
        """
        I don't know if there is a way to guarantee that an orchestration will
        be deployed or not. So for now, this method will not be implemented.
        profile -- the resources needed
        """
        return True

    def allocate_resources(self, platform, profile):
        """
        Deploy the template stack. Retrieve the ID from heat and insert it into
        the platform
        profile -- the resources needed
        """
        tenant_id = get_tenant_id(self.auth_url + "/tenants", self.token, self.tenant_name)
        heat_base_url = "http://" + self.auth_url.split(":")[1][2:] + ":8004/v1"
        stack_name = profile.keys()[0]
        template_file = profile.values()[0]['template']
        params = profile.values()[0]['parameters']
        params['key'] = self.key

        stack_id = create_stack(token = self.token, tenant_id = tenant_id, heat_base_url = heat_base_url,
                     stack_name = stack_name, template_file = template_file, params = params)

        platform.set_allocation_id(stack_name + ":" + stack_id)
        platform.set_status("BUILDING")
        return stack_id

    def allocation_status(self, platform):
        """
        How is the stack creation going? This should update the platform object.
        platform -- the platform that needs the resources
        """
        tenant_id = get_tenant_id(self.auth_url + "/tenants", self.token, self.tenant_name)
        heat_base_url = "http://" + self.auth_url.split(":")[1][2:] + ":8004/v1"
        stack_name = platform.get_allocation_id().split(":")[0]
        stack_id = platform.get_allocation_id().split(":")[1]

        status = status_stack(token = self.token, tenant_id = tenant_id, heat_base_url = heat_base_url,
                     stack_name = stack_name, stack_id = stack_id)

        platform.set_status(status)
        return status

    def deallocate_resources(self, platform):
        """
        Destroy the stack.
        platform -- the platform that was using the resources
        """
        tenant_id = get_tenant_id(self.auth_url + "/tenants", self.token, self.tenant_name)
        heat_base_url = "http://" + self.auth_url.split(":")[1][2:] + ":8004/v1"
        stack_name = platform.get_allocation_id().split(":")[0]
        stack_id = platform.get_allocation_id().split(":")[1]

        status = delete_stack(token = self.token, tenant_id = tenant_id , heat_base_url = heat_base_url ,
                      stack_name = "teste", stack_id = stack_id)
        return status

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

    def status_stack(token, tenant_id, heat_base_url, stack_name, stack_id):
        headers = {'X-Auth-Token': token}
        r = requests.get(heat_base_url + "/" + tenant_id + "/stacks/" + stack_name + "/" + stack_id, headers = headers)
        return r.json()

    def delete_stack(token, tenant_id, heat_base_url, stack_name, stack_id):
        headers = {'X-Auth-Token': token}
        r = requests.delete(heat_base_url + "/" + tenant_id + "/stacks/" + stack_name + "/" + stack_id, headers = headers)
        return r.status_code

def main():
   properties = {
      'credentials': "keystonerc_admin",
      'key': "joaoalencar",
      'username': "joaoalencar",
      'password': "XXXXXXX",
      'auth_url': "http://200.19.177.89:5000/v2.0",
      'tenant_name': "hpcshelf",
      'region_name': "RegionOne"
   }

   profile = {
      'liacloud_low': {
         'id': 0,
         'template': "cluster.yaml",
         'parameters': {
            'image': "Ubuntu1404"
            'flavor': "hpcshelf.medium"
            'public_network': "ext-net"
            'cluster_size': 2
         }
      }
   }

   lia = OpenStack(properties)
   lia.authenticate()

   p = Platform(0, 0, "", "BUILDING")
   print "Initial Platform: "
   print p
   if lia.verify_profile_availability(profile):
       allocation_id = lia.allocate_resources(p, profile)
       p.set_allocation_id(allocation_id)
       print "After Allocation "
       print p
       print lia.allocation_status(p)
       print "After Status Update "
       print p
       lia.deallocate_resources(p)
       print "After Deallocation "
       print p
   else:
       print "Insuffiecient Resources..."

if __name__ == "__main__":
   main()
