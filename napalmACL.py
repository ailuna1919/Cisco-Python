#You need to add the following command to the Cisco device:
#ip scp server enable

#Example:
#S1(config)#ip scp server enable

import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.84', 'cisco', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.84')
iosvl2.load_merge_candidate(filename='ACL1.cfg')
iosvl2.commit_config()
iosvl2.close()


