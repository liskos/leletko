import ipaddress

net = ipaddress.ip_network("192.168.76.160/255.255.255.240", 0)
k = 0
for ip in net.hosts():
    if int(ip.__format__("b")[-4:], 2) % 2 == 0 and ip.packed[3].__format__("b").count("1") % 2 == 0:
        k += 1

print(k)