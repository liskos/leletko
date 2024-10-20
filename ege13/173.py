import ipaddress

ip = ipaddress.ip_address("190.120.251.78")
for m in range(10,32):
    net = ipaddress.ip_network(f"190.120.251.78/{m}", 0)
    print(net)