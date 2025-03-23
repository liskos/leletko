def f(n):
    s = str(n)
    while "111" in s or "88888" in s:
        if "111" in s:
            s = s.replace("111", "88")
        if "88888" in s:
            s = s.replace("88888", "8")
    return s

a = "1" * 81
print(f(a))