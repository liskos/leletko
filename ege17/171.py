def p(n, s):
    b = ""
    while n > 0:
        b = b + str(n % s)
        n = n // s
    return b[::-1]

a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if p(x,3)[-1] == p(x,5)[-1] and x % 31 == 0 and (x % 47 == 0 or x % 53 == 0)]
print(len(b), min(b))

