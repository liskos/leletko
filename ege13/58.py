import ipaddress

ip = ipaddress.ip_address("134.92.108.145")
for m in range(10,32):
    net = ipaddress.ip_network(f"134.92.104.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)