import ipaddress

net = ipaddress.ip_network("98.71.254.171/255.248.0.0", 0)
last = net[-1]
for i in net:
    if i.__format__("b").count("1") % 5 == 0 and i != last:
        print(i)