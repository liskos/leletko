import ipaddress

ip = ipaddress.ip_address("108.133.75.91")
for m in range(10,32):
    net = ipaddress.ip_network(f"108.133.75.64/{m}", 0)
    if ip in net:
        print(net, len(list(net)))