def f(s:str):
    while "33333" in s or "1111" in s:
        if "33333" in s:
            s = s.replace("33333", "111", 1)
        else:
            s = s.replace("111", "33",1)
    return s


a = "3" * 234
z = f(a)
o = 1
for x in z:
    o = o * int(x)

print(o)