from ncclient import manager
import xmltodict
import xml.dom.minidom
import xml.etree.ElementTree as ET

m = manager.connect(
    host="sandbox-iosxe-latest-1.cisco.com",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

'''
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
'''
'''
netconf_reply = m.get_config(source='running')
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''
netconf_filter = """
<filter type="subtree">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
