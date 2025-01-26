a = [int(x) for x in open("17.txt")]
b = len([x for x in a if str(x)[-1] == "7"])
r = []
for i in range(len(a) - 1):
    if (str(a[i]) + str(a[i+1])).count("-") == 1 and (a[i] + a[i+1]) < b:
        r.append(a[i] + a[i+1])

print(len(r), max(r))