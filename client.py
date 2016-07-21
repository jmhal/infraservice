import time

import suds
client = suds.client.Client('http://localhost:8000/backend/wsdl', cache=None)

# Show profiles
print "Profiles:"
profiles = client.service.available_profiles()[0]
for profile in profiles:
   print profile

# Create a platform for each profile
print "Creating one platform for each profile..."
for profile in profiles:
   client.service.deploy_contract(profile['profile_id'])

# Retrieve and show all the available platforms
print "Available platforms:"
platforms = client.service.available_platforms()
#print platforms
for platform in platforms[0]:
    print platform

# Wait until each platform is ready
for platform in platforms[0]:
    status = "BUILDING"
    while status != "CREATED" :
        status = client.service.platform_deployment_status(platform['platform_id'])
        print "Building platforms..."
        time.sleep(5)
    print platform['platform_id'] + ", " + status

# Destroy each plaftorm
print "Destroying platforms..."
for platform in platforms[0]:
    status = client.service.destroy_platform(platform['platform_id'])
    print platform['platform_id'] + ", " + status

# Retrieve and show all the available platforms
print "Available platforms:"
try :
   platforms = client.service.available_platforms()
   for platform in platforms[0]:
       print platform
except IndexError:
    print "No platforms"
