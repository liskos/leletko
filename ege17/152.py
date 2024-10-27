def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 8)
        n = n // 8
    return b[::-1]

a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(len(a) - 1):
    if a[i] > 0 and a[i + 1] > 0:
        if (a[i] % 9 == 0 and f(a[i + 1])[-1] == "3" and a[i + 1] % 9 != 0) or (f(a[i])[-1] == "3" and a[i + 1] % 9 == 0 and a[i] % 9 != 0):
            r.append(max(a[i], a[i +1]))
print(len(r), max(r))