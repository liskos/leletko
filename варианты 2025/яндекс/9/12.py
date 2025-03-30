import itertools

def su(n):
    n = int(n)
    s = 0
    while n > 0:
        s = s + n % 10
        n = n  // 10
    return s


def f(s:str):
    while "53" in s or "63" in s:
        if "63" in s:
            s = s.replace("63", "72", 1)
        else:
            s = s.replace("53", "91", 1)
    return s

a = "53" * 25 + "63" * 15 + 5 * "6"
print(su(f(a)))