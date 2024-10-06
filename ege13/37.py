import  ipaddress

net = ipaddress.ip_network("206.158.124.67/255.255.224.0", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-13:], 2))