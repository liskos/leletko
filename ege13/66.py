import ipaddress

ip = ipaddress.ip_address("214.228.114.203")
for m in range(10,32):
    net = ipaddress.ip_network(f"214.228.96.0/{m}", 0)
    if ip in net:
        print(net,net.netmask)