import  ipaddress

ip = ipaddress.ip_address("121.171.15.149")
for m in range(10,32):
    net = ipaddress.ip_network(f"121.171.15.143/{m}", 0)
    if ip in net:
        print(net, len(list(net.hosts())))