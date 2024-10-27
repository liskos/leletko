def p(n, s):
    b = ""
    while n > 0:
        b = b + str(n % s)
        n = n // s
    return b[::-1]

a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if bin(x)[-4:] == "1001" and p(x,5)[-2:] == "11"]
print(max(b), sum(b))
