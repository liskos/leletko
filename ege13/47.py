import ipaddress

net = ipaddress.ip_network("224.24.254.134/255.255.224.0", 0)
print(net)