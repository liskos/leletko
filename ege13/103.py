import ipaddress

ip = ipaddress.ip_address("214.224.120.40")
for m in range(10,32):
    net = ipaddress.ip_network(f"214.224.120.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)