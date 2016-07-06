#!/home/jmhal/heatclient/bin/python
from heatclient.common import template_format
from heatclient.common import template_utils
import json



def get_fields(template_file, params):
    tpl_files, template = template_utils.get_template_contents(template_file = template_file)
    fields = {
        'stack_name': 'teste',
        'parameters': params,
        'template': template,
        'files': dict(list(tpl_files.items())),
    }
    return fields

template_file = "/home/jmhal/repositorios/infraservice/tests/heat_templates/cluster.yaml"

params = {}
params['image'] = 'Ubuntu1404'
params['flavor'] = 'shelf.medium'
params['key'] = 'joaoalencar'
#params['private_network'] = 'demo-net'
params['public_network'] = 'ext-net'
params['cluster_size'] = '4'

print json.dumps(get_fields(template_file,params))
