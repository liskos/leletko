import ipaddress

ip = ipaddress.ip_address("229.117.114.172")
for m in range(10,32):
    net = ipaddress.ip_network(f"229.117.114.172/{m}", 0)
    print(net)