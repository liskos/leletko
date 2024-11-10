def f(n):
    b = ""
    while n > 0:
        b = b + str(n%6)
        n = n // 6
    return b.count("0")


a = [int(x) for x in open("17data/17-290.txt")]
c = []
for i in range(len(a)- 2):
    if a[i] % 5 == 4 or a[i+1] % 5 == 4 or a[i+2] % 5 == 4:
        if f(a[i]) == f(a[i+1]) == f(a[i+2]) == 0:
            c.append(max(a[i:i+3]) - min(a[i:i+3]))

print(len(c), max(c))