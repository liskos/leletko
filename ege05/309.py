def f(n):
    s = ''
    z = n
    while z > 0:
        s1 = bin(z % 10)[2:]
        s = '0' * (4 - len(s1)) + s1 + str(s1.count('1') % 2) + s
        z //= 10
    s = '1' + s[2:] + '0'
    return int(s, 2)


for i in range(1, 10000):
    if f(i) == 674890:
        print(i)