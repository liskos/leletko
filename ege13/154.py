import ipaddress

ip = ipaddress.ip_address("125.28.160.73")
for m in range(10,32):
    net = ipaddress.ip_network(f"125.28.160.0/{m}", 0)
    if ip in net and len(list(net)) >= 500 and ip in net.hosts():
        print(net, net.netmask)
