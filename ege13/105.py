import ipaddress

ip = ipaddress.ip_address("125.181.67.15")
for m in range(10,32):
    net = ipaddress.ip_network(f"125.181.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)