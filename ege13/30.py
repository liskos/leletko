import  ipaddress

net = ipaddress.ip_network("156.128.0.227/255.255.255.248", 0)
print(net)
for  ip in net:
    print(ip, int(ip.__format__("b")[-3:], 2))