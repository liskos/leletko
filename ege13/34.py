import  ipaddress

net = ipaddress.ip_network("156.132.15.138/255.255.252.0", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-3:], 2))