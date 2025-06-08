import ipaddress
ip = ipaddress.ip_address("192.214.116.184")
for m in range(33):
    net = ipaddress.ip_network(f"192.214.116.184/{m}",0)
    if ip in net and net[0].__format__("b").count("1") % 5 == 0 and ip != net[0]:
        print(net[0])
