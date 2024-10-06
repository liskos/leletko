import  ipaddress

net = ipaddress.ip_network("192.168.156.235/255.255.255.240", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-3:], 2))