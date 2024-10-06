import ipaddress

ip = ipaddress.ip_address("135.116.177.140")
for m in range(10,32):
    net = ipaddress.ip_network(f"135.116.160.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)