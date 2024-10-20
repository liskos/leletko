import ipaddress

k = 0
net = ipaddress.ip_network("192.168.32.160/255.255.255.240", 0)
for ip in net:
    if ip.__format__("b").count("0") > 21:
        k += 1
print(k)