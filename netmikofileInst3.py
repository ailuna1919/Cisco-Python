from netmiko import ConnectHandler

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.200',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.87',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.89',
    'username': 'cisco',
    'password': 'cisco',
}

try:
   with open('iosv_l2_cisco_design') as f:
       lines = f.read().splitlines()
   print (lines)
except:
    print("[!!!!] Cannot Open the File ... ")
    exit()

all_devices = [iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    try:
       print("\n......Configuring Device  " + devices['ip'], "\n")
       net_connect = ConnectHandler(**devices)
       output = net_connect.send_config_set(lines)
       print (output)
    except:
        print("[!!!!] Cannot connect to the SSH Server:   ", devices['ip'])
        pass