a = [int(x) for x in open("17data/17-4.txt")]
r = []
k = 0
for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 7 != 0 and a[i] % 17 != 0 and a[i] % 19 != 0 and a[i] % 27 !=0:
        r.append(a[i])
print(len(r), max(r))