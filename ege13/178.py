import ipaddress

ip = ipaddress.ip_address("120.216.74.153")
for m in range(10,32):
    net = ipaddress.ip_network(f"120.216.74.153/{m}", 0)
    print(net, len(list(net)))