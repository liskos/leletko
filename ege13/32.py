import  ipaddress

net = ipaddress.ip_network("10.18.134.220/255.255.255.192", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-6:], 2))