import itertools
def proverka(n, a):
    if n in a:
        return True
    if not a:
        return False
    b = [i for i in a if i <= n]
    for i in b:
        c = b.copy()
        c.remove(i)
        if proverka(n - i, c):
            return True
    return False


def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = sorted([int(file.readline()) for _ in range(n)])
    print(n, a)
    if n in a:
        return True
    if not a:
        return False
    for i in range(174, sum(a)+1):
        if proverka(i, [x for x in a if x <= i]):
            print(i, "ok")
        else:
            print(i, "no ok")
            break
    return i, 0





print(f("26test.txt"))  #6 4  (7 8 9 100)
print("------------------")
print(f("26(1).txt"))

