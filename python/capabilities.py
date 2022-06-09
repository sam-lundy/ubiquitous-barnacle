from ncclient import manager
import logging

#logging.basicConfig(level=logging.DEBUG)

router = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": "830",
    "username": "developer",
    "password": "C1sco12345"
}

with manager.connect(**router, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 25)
        print(' ')
        print(capability)





##This is a comment