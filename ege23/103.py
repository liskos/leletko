def f(a, b, k):
    if a == b and k ==6:
        return 1
    if a > b:
        return 0
    return f(a+1, b, k+1) + f(a+2, b, k+1) + f(a*2, b, k+1)

print(f(1, 20, 0))