import ipaddress

net = ipaddress.ip_network("139.75.100.0/255.255.252.0", 0)
k = 0
for ip in net:
    for i in range(2, 11):
        if int(str(ip)[:-3:]) == 2 ** i - 1:
            print(ip)
print(k)