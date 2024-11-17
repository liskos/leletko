a = [int(x) for x in open("17.txt")]
k = []
m = max([x for x in a if str(x)[-2:] == "14"])

for i in range(len(a) - 2):
    if a[i] % 14 == 0 and a[i+1] % 14 == 0 and a[i+2] % 14 == 0 and (a[i]+a[i+1]+a[i+2]) > (m * 2):
        print(i)
        k.append(sum(a[i:i+3]))

print(len(k), min(k))