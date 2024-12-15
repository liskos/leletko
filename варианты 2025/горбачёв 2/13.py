import ipaddress

ip = ipaddress.ip_address("82.230.106.168")
net = ipaddress.ip_network("82.230.106.168/255.255.255.240", 0)
k = 0
for i in net:
    if i.__format__("b")[7:24].count("1") % 3 == 0:
        k += 1
print(k)