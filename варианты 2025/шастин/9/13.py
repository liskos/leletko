import ipaddress
r = []

for m in range(32):
    net = ipaddress.ip_network(f"111.233.75.16/{m}", 0)
    print(net)

for m in range(24,28):
    k = 0
    net1 = ipaddress.ip_network(f"111.233.75.16/{m}", 0)
    for ip in net1:
        k += 1
    r.append(k)

print(max(r))