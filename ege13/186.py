import ipaddress

k = 0
net = ipaddress.ip_network("90.65.32.0/255.255.224.0", 0)
for ip in net:
    if ip.__format__("b").count("1") == ip.__format__("b").count("0"):
        k += 1
print(k)