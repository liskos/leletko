def f(n):
    n = int(n)
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


a = [int(x) for x in open("17data/17-8.txt")]
r = []
k = 0
for i in range(len(a) -2):
    if (f(bin(a[i])[2:]) > 5 and f(bin(a[i])[2:]) % 2 == 0) or (f(bin(a[i+1])[2:]) > 5 and f(bin(a[i+1])[2:]) % 2 == 0):
        r.append(a[i] + a[i+1])
print(len(r), max(r))