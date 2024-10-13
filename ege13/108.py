import ipaddress

ip = ipaddress.ip_address("218.217.212.15")
for m in range(10,32):
    net = ipaddress.ip_network(f"218.217.192.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)