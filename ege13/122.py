import ipaddress

ip = ipaddress.ip_address("106.113.64.105")
for m in range(10,32):
    net = ipaddress.ip_network(f"106.113.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)