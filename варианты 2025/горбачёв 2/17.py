a = [int(x) for x in open("17.txt")]
s = len([x for x in a if x < 0 and abs(x) % 5 == 0])
r = []
for i in range(len(a)-2):
    d = str(len(str(abs(a[i])))) + str(len(str(abs(a[i+1])))) + str(len(str(abs(a[i+2]))))
    if d.count("4") >= 2 and a[i] + a[i+1] + a[i+2] >= s:
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), min(r))