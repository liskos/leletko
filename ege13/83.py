import ipaddress

ip = ipaddress.ip_address("115.12.69.38")
for m in range(10,32):
    net = ipaddress.ip_network(f"115.12.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)