import ipaddress

net = ipaddress.ip_network("158.132.161.128/255.255.255.128", 0)
k = 0
for ip in net:
    if ip.__format__("b")[-1] == "1":
        k += 1
print(k)