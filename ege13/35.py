import  ipaddress

net = ipaddress.ip_network("112.154.133.208/255.255.248.0", 0)
print(net)
for ip in net:
    print(ip, int(ip.__format__("b")[-11:], 2))