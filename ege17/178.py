def d(n):
    k = 0
    if n % 2 == 0:
        k += 1
    if n % 3 == 0:
        k += 1
    if n % 5 == 0:
        k += 1
    if n % 7 == 0:
        k += 1
    return k



a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if d(x) == 2]
print(len(b), max(b) + min(b))