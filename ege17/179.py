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
b = [x for x in a if str(x)[-1] == "2" or str(x)[-1] == "7" and x % 3 == 0 and x % 11 == 0]
print(len(b), min(b))