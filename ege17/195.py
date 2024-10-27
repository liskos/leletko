a = [int(x) for x in open("17data/17-9.txt")]
r = []
for i in range(len(a) - 2):
    k = 0
    if bin(a[i])[2:].count("1") >= 3 and bin(a[i])[2:].count("0") >= 1:
        k += 1
    if bin(a[i+1])[2:].count("1") >= 3 and bin(a[i+1])[2:].count("0") >= 1:
        k += 1
    if bin(a[i+2])[2:].count("1") >= 3 and bin(a[i+2])[2:].count("0") >= 1:
        k += 1
    if k >= 2:
        r.append(max(a[i], a[i+2], a[i+2]))

print(len(r), max(r))