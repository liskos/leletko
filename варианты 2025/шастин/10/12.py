def f(s:str):
    k = 0
    while "4444" in s or "222" in s:
        if "4444" in s:
            s = s.replace("4444", "2",1)
            k += 1
        else:
            if "222" in s:
                k += 1
            s = s.replace("222","44",1)
    return k


a = 222 * "4"
print(f(a))