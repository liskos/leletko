import ipaddress

net = ipaddress.ip_network("136.36.240.16/255.255.255.248", 0)
for i in net:
    if "101" not in i.__format__("b"):
        print(i.__format__("b"))
