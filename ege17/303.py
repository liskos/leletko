def k(n):
    return (int(n ** (1/3))) ** 3 == n

def f(n):
    return (int(n ** (0.5))) ** 2 == n

a = [int(x) for x in open("17data/17-303.txt")]
c = []
m = max([x for x in a if k(x)])
for i in range(len(a) - 2):
    if f(abs(m - (a[i] + a[i+1] + a[i+2]))) and abs(m - (a[i] + a[i+1] + a[i+2])) % 2 == 0:
        c.append(a[i] + a[i+1] + a[i+2],)
        if a[i] + a[i+1] + a[i+2] == 23229:
            print(a[i], a[i+1], a[i+2])
print(len(c), 5626 * 8177, c)