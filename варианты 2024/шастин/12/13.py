from ipaddress import *
k = 0
net = ip_network("192.168.72.128/255.255.255.128")
for ip in net:
    if ip.__format__("b").count("1") % 10 == 0:
        k += 1
print(k)