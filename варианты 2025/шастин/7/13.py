import ipaddress
ip1 = ipaddress.ip_address("200.154.190.12")
ip2 = ipaddress.ip_address("200.154.184.0")

for m in range(10,32):
    net = ipaddress.ip_network(f"200.154.184.0/{m}", 0)
    if ip1 in net and ip2 in net and net[-1] != ip1 and net[-1] != ip2:
        if net[0] != ip1 and net[0] != ip2:
            print(m)