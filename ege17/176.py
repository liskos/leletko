def s(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if s(x) >= 15 and x % 3 != 0 and x % 4 != 0 and x % 7 != 0]
print(min(b), sum(b))