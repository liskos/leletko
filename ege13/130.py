import ipaddress

ip = ipaddress.ip_address("156.133.216.35")
for m in range(10,32):
    net = ipaddress.ip_network(f"156.133.216.0/{m}", 0)
    if ip in net:
        print(net, len(list(net)))