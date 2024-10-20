import ipaddress

ip = ipaddress.ip_address("111.3.161.27")
for m in range(10,32):
    net = ipaddress.ip_network(f"111.3.160.0/{m}", 0)
    if ip in net and len(list(net)) >= 2000 and ip in net.hosts():
        print(net, len(list(net)), net.netmask)

