a = [int(x) for x in open("17data/17-9.txt")]
r = []
for i in range(len(a) - 2):
    tr = a[i:i +3]
    b = [bin(x)[2:] for x in tr if bin(x)[2:].count("1") == 2 and bin(x)[2:].count("0") >= 1]
    if len(b) >= 2:
        r.append(max(tr))

print(len(r), sum(r))
