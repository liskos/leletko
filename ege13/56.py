import ipaddress

ip = ipaddress.ip_address("153.209.31.240")
for m in range(10,32):
    net = ipaddress.ip_network(f"153.209.28.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)