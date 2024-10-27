a = [int(x) for x in open("17data/17-7.txt")]
r = []
for i in range(len(a)):
    if hex(a[i])[-1] == "9" and hex(a[i])[-2:] != "a9":
        r.append(a[i])
print(len(r), max(r))