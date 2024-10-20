import ipaddress

k = 0
net = ipaddress.ip_network("154.233.0.0/255.255.0.0", 0)
for ip in net:
    if ip.__format__("b")[-1] == "0":
        k += 1
print(k)