import ipaddress

ip = ipaddress.ip_address("115.53.128.88")
for m in range(10,32):
    net = ipaddress.ip_network(f"115.53.128.0/{m}", 0)
    if ip in net and len(list(net)) >= 1000 and ip in net.hosts():
        print(net, net.netmask)
