a = [int(x) for x in open("17.txt")]
m = min([x for x in a if str(x)[-1] == "7"])
r = []
for i in range(len(a) - 2):
    p = a[i] * a[i+1] * a[i+2]
    if len(str(abs(a[i]))) == 5 or len(str(abs(a[i+1]))) == 5 or len(str(abs(a[i+2]))) == 5:
        if abs(p) % abs(m) == 0:
            r.append(p)

print(len(r), max(r))