import ipaddress

k = 0
ip = ipaddress.ip_address("222.121.128.0")
net = ipaddress.ip_network("222.121.128.0/255.255.224.0", 0)
for i in net:
    if i.__format__("b")[-1] == i.__format__("b")[-2]:
        k += 1

print(k)