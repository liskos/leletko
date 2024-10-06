import  ipaddress

net = ipaddress.ip_network("126.185.90.162/255.255.252.0", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-10:], 2))