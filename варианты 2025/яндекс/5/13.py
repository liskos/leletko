import ipaddress

ip = ipaddress.ip_address("137.219.220.63")

for m in range(32):
    net = ipaddress.ip_network(f"137.219.220.63/{m}", 0)
    if ip != net[-1]:
        print(m)