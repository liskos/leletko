def f(n):
    if str(n)[-2:] == "42" and len(str(abs(n))) == 4:
        return 1
    else:
        return 0

a = [int(x) for x in open("17.txt")]
m = max([x for x in a if abs(x) % 42 == 0 and len(str(abs(x))) == 4])
c = []
for i in range(len(a)- 2):
    if f(a[i]) + f(a[i+1]) + f(a[i+2]) >= 2 and (a[i] + a[i+1] + a[i+2]) > m:
        c.append(sum(a[i:i+3]))

print(len(c), max(c))