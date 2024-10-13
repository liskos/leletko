import ipaddress

ip = ipaddress.ip_address("215.118.70.47")
for m in range(10,32):
    net = ipaddress.ip_network(f"215.118.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)