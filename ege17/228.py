a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 2):
    c = [ x for x in a[i:i+3] if x < sr]
    d = [ x for x in a[i:i+3] if x % 3== 0]
    if (len(c) >= 1) and (len(d) >= 1):
        r.append(sum(a[i:i+3]))

print(len(r), max(r))