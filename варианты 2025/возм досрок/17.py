a = [int(x) for x in open("17.txt")]
m = min([x for x in a if len(str(abs(x))) == 4 and abs(x) % 17 == 0])**2
r = []
for i in range(len(a)-2):
    if (len(str(abs(a[i]))) == 4 and abs(a[i]) % 100 == 27) or (len(str(abs(a[i+1]))) == 4 and abs(a[i+1]) % 100 == 27) or (len(str(abs(a[i+2]))) == 4 and abs(a[i+2]) % 100 == 27):
        if (a[i]**2 + a[i+1]**2 + a[i+2]**2) <= m:
            r.append(abs(a[i]) + abs(a[i+1]) + abs(a[i+2]))

print(len(r), min(r))
