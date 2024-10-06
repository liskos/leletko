import  ipaddress

net = ipaddress.ip_network("162.198.0.157/255.255.255.224", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-3:], 2))