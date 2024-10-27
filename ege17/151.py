a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(len(a) - 1):
    if (str(a[i])[-1] == "6" and a[i] % 3 == 0) or (str(a[i + 1])[-1] == "6" and a[i + 1] % 3 == 0):
        r.append(min(a[i], a[i +1]))
print(len(r), min(r))