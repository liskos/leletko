def f(a, b, k):
    if a == b and k ==0:
        return 1
    if a > b or k <0:
        return 0
    return f(a+1, b, k-1) + f(a+5, b, k-1) + f(a*3, b, k-1)

for k in range(1, 100):
    if f(1, 227, k) != 0:
        print(k)
        break