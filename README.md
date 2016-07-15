# InfraService
A service for managing computational infrastructures like clusters, clouds and grids. 

## Setting environment for development

I'm using either Fedora 24 or Ubuntu 14.04. The basic requirement is Python 2.7.x. The best way to proceed is to use a virtualenv environment. There you can install any Python package without root credentials. 

`$ mkdir virtualenv`

`$ virtualenv virtualenv/infraservice`

`$ source virtualenv/infraservice/bin/activate`

Install the distro packages for OpenSSL development (something like openssl-devel) and development libraries for XML (something like libxslt-devel and libxml-devel)

`$ pip install paramiko python-heatclient django pyws suds` 

`$ mkdir repositorios`

`$ git clone https://github.com/jmhal/infraservice repositorios/infraservice`



