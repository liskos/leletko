def s(n):
    n = int(n[:-1])
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s



def f(s):
    s = str(s)
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    return s


for n in range(7,100):
    a = ">" + 19 * "0" + n * "1" + 19 * "2"
    if str(s(f(a)))[-2] == str(s(f(a)))[-1]:
        print(n)
