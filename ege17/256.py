def f(n):
    b = ""
    while n > 0:
        b = b + str(n%7)
        n = n // 7
    return b[::-1]

a = [int(x) for x in open("17data/17-243.txt")]
m = max(x for x in a if x % 107 == 0)
b = []
for i in range(len(a)- 1):
    if (a[i] > m or a[i+1] > m) and (f(a[i]).count("36") >= 1 or f(a[i+1]).count("36") >= 1):
        b.append(a[i] + a[i+1])

print(len(b), min(b))