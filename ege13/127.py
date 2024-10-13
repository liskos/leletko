import ipaddress

ip = ipaddress.ip_address("111.81.200.27")
for m in range(10,32):
    net = ipaddress.ip_network(f"111.81.192.0/{m}", 0)
    if ip in net:
        print(net, len(list(net)))