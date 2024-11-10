def f(a, b):
    global s
    return (a > s) and b <= s and b % 10 == 7

a = [int(x) for x in open("17data/17-243.txt")]
s = sum(sum(int(i) for i in str(x)) for x in a if x % 49 == 0)
b = []
for i in range(len(a)- 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        b.append(a[i] + a[i+1])

print(len(b), min(b))