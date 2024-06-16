a = [int(x) for x in open("17.txt")]
m121 = max([x for x in a if str(x)[-3:] == "121"])


k = []
for i in range(len(a)-2):
    z = a[i:i+3]
    x = [x for x in z if len(str(abs(x))) == 4 and abs(x) % 2 == 0]
    if len(x) <= 1 and sum(z) <= m121:
        k.append(sum(z))
print(len(k))
print(max(k))