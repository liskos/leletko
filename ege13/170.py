import ipaddress

net = ipaddress.ip_network("174.114.120.0/255.255.252.0", 0)
k = 0
for ip in net:
    ip1 = ip.__format__("b")
    if str(ip1).count("1") % 2 == 0:
        print(ip)
        k += 1
print(k)