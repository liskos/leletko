def p(n):
    b = ""
    while n > 0:
        b = b = str(n % 3)
        n = n // 3
    return b[::-1]

def s(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if s(x) % 5 == 0 and p(x)[-2:] != "00"]
print(len(b), max(b))
