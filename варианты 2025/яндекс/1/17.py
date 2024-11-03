a = [int(x) for x in open("17.txt")]
m = len([x for x in a if x % 2042 == 0])
r = []
for i in range(len(a)- 1):
    if a[i]+ a[i+1] > m:
        r.append(a[i] + a[i+1])

print(len(r), max(r))
