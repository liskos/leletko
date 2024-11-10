def k(n):
    return (int(n ** 0.5)) ** 2 == n

def f(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

a = [int(x) for x in open("17data/17-302.txt")]
c = []
m = min([x for x in a if x % 21 == 0])
for i in range(len(a)- 2):
    if f(abs(((a[i] + a[i+1]) / 2) - m)):
        c.append(a[i] * a[i+1])
print(len(c), min(c))