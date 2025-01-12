def f(n):
    s = str(n)
    while "888" in s or "2222" in s:
        if "2222" in s:
            s = s.replace("2222", "88")
        if "888" in s:
            s = s.replace("888", "22")
    return s

print(f("8" * 140))