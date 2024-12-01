def f(s):
    while "111" in s or "88" in s:
        if "88" in s:
            s = s.replace("88", "1111")
        else:
            s = s.replace("111", "8")
    return s

a = "1" * 81
print(f(a))