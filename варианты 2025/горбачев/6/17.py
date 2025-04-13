a = [int(x) for x in open("17.txt")]
m = min([x for x in a if abs(x) % 10 == 7 and abs(x) % 7 == 0])
print(m)
r = []

for i in range(len(a)-1):
    if len(str(abs(a[i]))) == 3 or len(str(abs(a[i+1]))) == 3:
        if a[i] + a[i+1] > m:
            r.append(a[i]**2 + a[i+1]**2)

print(len(r), max(r))