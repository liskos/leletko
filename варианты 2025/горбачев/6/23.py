def f(a,b):
    if a == b:
        return 1
    if a > b or a == 0:
        return 0
    if a < 0:
        return f(a+3,b) + f(a+4,b) + f(abs(a),b)
    return f(a + 3, b) + f(a + 4, b)

print(f(-21,-8)*f(-8,35))