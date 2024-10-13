import ipaddress

ip = ipaddress.ip_address("192.75.64.98")
for m in range(10,32):
    net = ipaddress.ip_network(f"192.75.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)