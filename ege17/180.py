def p(n, s):
    b = ""
    while n > 0:
        b = b + str(n % s)
        n = n // s
    return b[::-1]

a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if p(x, 5)[-1] == "3" and p(x, 9)[-1] == "5" and p(x, 8)[-1] != "7"]
print(len(b), max(b))