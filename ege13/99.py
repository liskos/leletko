import ipaddress

ip = ipaddress.ip_address("193.138.70.47")
for m in range(10,32):
    net = ipaddress.ip_network(f"193.138.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)