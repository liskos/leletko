import ipaddress

ip = ipaddress.ip_address("175.122.80.13")
for m in range(10,32):
    net = ipaddress.ip_network(f"175.122.80.0/{m}", 0)
    if ip in net and len(list(net)) >= 60 and ip in net.hosts():
        print(net, net.netmask)