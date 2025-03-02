import ipaddress

net1 = ipaddress.ip_network("192.168.56.192/255.255.255.192",0)
net2 = ipaddress.ip_network("192.168.56.208/255.255.255.240", 0)
k = 0
for ip1 in net1:
    if all(ip1 != ip2 for ip2 in net2):
        k += 1
print(k)