def f(n):
    s = ""
    for x in str(n):
        s += bin(int(x))[2:].zfill(4)
    s = s.replace("1","2")
    s = s.replace("0","1")
    s = s.replace("2", "0")
    return int(s, 2)


for i in range(1, 1000):
    if f(i) == 151:
        print(i)
print(f(13))
