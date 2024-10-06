import  ipaddress

net = ipaddress.ip_network("132.126.150.18/255.255.240.0", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-12:], 2))