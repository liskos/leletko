import  ipaddress

ip = ipaddress.ip_address("112.117.107.70")
for m in range(10,32):
    net = ipaddress.ip_network(f"112.117.121.80/{m}", 0)
    if ip in net:
        print(net, len(list(net)))