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
        pass

    def allocate_resources(self, platform, profile):
        """
        Deploy the template stack. Retrieve the ID from heat and insert it into
        the platform
        profile -- the resources needed
        """
        pass

    def allocation_status(self, platform):
        """
        How is the stack creation going? This should update the platform object.
        platform -- the platform that needs the resources
        """
        pass

    def deallocate_resources(self, platform):
        """
        Destroy the stack.
        platform -- the platform that was using the resources
        """
        pass

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
