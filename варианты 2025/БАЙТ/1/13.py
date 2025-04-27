import ipaddress

net1 = ipaddress.ip_network("192.168.100.0/255.255.255.240", 0)
net2 = ipaddress.ip_network("192.168.100.16/255.255.255.240", 0)
for m in range(1,32):
    net3 = ipaddress.ip_network(f"192.168.100.0/{m}", 0)
    if all(ip in net3 for ip in net1) and all(ip1 in net3 for ip1 in net2):
        print(m)

print(int("11100000",2))