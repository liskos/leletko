import  ipaddress

net = ipaddress.ip_network("122.191.12.189/255.255.255.128", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-7:], 2))