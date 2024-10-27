def f(a, b):
    return a % 9 == 0 and abs(b) % 8 == 3 and b % 9 != 0

a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        r.append(max(a[i], a[i +1]))
print(len(r), max(r))