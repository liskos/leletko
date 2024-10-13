import ipaddress

ip = ipaddress.ip_address("131.149.64.13")
for m in range(10,32):
    net = ipaddress.ip_network(f"131.149.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)