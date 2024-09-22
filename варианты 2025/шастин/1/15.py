def f(x, y, A):
    return (x <= 19) or ( y < 2 * x + A - 50) or (y > 17)

for A in range(0, 1000):
    if all(f(x, y, A) == 1 for x in range(1000) for y in range(1000)):
        print(A)
        break