def f(a):
    if a in [50,51,52,53,54]:
        return 1
    if a > 60 or a == 23:
        return 0
    return f(a+3) + f(a+4) + f(a*2)

print(f(11))

