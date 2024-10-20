import ipaddress

ip = ipaddress.ip_address("193.22.209.132")
for m in range(10,32):
    net = ipaddress.ip_network(f"193.22.209.132/{m}", 0)
    print(net)