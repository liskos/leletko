import ipaddress

ip = ipaddress.ip_address("153.209.23.240")
for m in range(10,32):
    net = ipaddress.ip_network(f"153.209.20.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)