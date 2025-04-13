import ipaddress
for a in range(1,255):
    ip1 = ipaddress.ip_address(f"135.{a}.170.5")
    net = ipaddress.ip_network(f"135.{a}.170.5/255.255.0.0", 0)
    if ip1 in net and all(ip.__format__("b")[:16].count("1") > 10 for ip in net):
        print(a)