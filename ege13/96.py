import ipaddress

ip = ipaddress.ip_address("204.108.112.142")
for m in range(10,32):
    net = ipaddress.ip_network(f"204.108.64.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)