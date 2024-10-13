import ipaddress

ip = ipaddress.ip_address("192.168.104.15")
for m in range(10,32):
    net = ipaddress.ip_network(f"192.168.104.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)