def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 8)
        n = n // 8
    return b[::-1]

a = [int(x) for x in open("17data/17-7.txt")]
r = []
k = 0
for i in range(len(a)):
    if f(a[i])[-1] == "7" and f(a[i])[-2:] != "27":
        r.append(a[i])
print(len(r), max(r))