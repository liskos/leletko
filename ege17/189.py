def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 3)
        n = n // 3
    return b[::-1]

a = [int(x) for x in open("17data/17-7.txt")]
r = []
k = 0
for i in range(len(a) -2):
    if f(a[i])[-1] == "2" or f(a[i+1])[-1] == "2" or f(a[i+2])[-1] == "2":
        r.append(min(a[i], a[i+1], a[i+2]))
print(len(r), sum(r))