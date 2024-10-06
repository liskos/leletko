import ipaddress

ip = ipaddress.ip_address("205.154.212.20")
for m in range(10,32):
    net = ipaddress.ip_network(f"205.154.192.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)