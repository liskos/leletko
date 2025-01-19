import ipaddress

ip1 = ipaddress.ip_address("105.241.51.30")
net = ipaddress.ip_network("105.241.51.30/255.255.248.0", 0)
k = 0
for ip in net:
    if ip.__format__("b").count("0") % 6 !=0:
        k += 1
print(k)