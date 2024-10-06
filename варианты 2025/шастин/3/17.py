def s(n):
    return sum(int(x) for x in str(abs(n)))


b = []
a = [int(x) for x in open("17.txt")]
m = min([x for x in a if x > 0 and x % 10 == 4])
for i in range(len(a) - 2):
    tr = a[i:i+3]
    if sum(s(t) for t in tr) == m:
        b.append(sum(tr))
print(len(b),max(b))