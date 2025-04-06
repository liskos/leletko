a = [int(x) for x in open("17.txt")]
m = max([x for x in a if len(str(abs(x))) == 3 and abs(x) % 100 == 33])
r = []

for i in range(len(a)-2):
    if (len(str(abs(a[i]))) == 5 and abs(a[i]) % 100 == 61) or (len(str(abs(a[i+1]))) == 5 and abs(a[i+1]) % 100 == 61) or (len(str(abs(a[i+2]))) == 5 and abs(a[i+2]) % 100 == 61):
        if a[i] + a[i+1] + a[i+2] >= m:
            r.append(a[i]+a[i+1]+a[i+2])

print(len(r), max(r))