import ipaddress

ip = ipaddress.ip_address("111.81.208.27")
for m in range(15,32):
    net = ipaddress.ip_network(f"111.81.192.0/{m}", 0)
    if ip in net:
        print(net, len(list(net)))