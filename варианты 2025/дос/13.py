import ipaddress

net = ipaddress.ip_network("143.168.72.213/255.255.255.240",0)
for ip in net:
    print(ip)