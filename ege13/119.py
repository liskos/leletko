import ipaddress

ip = ipaddress.ip_address("159.152.66.19")
for m in range(10,32):
    net = ipaddress.ip_network(f"159.152.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)