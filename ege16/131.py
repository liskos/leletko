
def f(n):
    if n == 2020:
        return 1
    if n > 1:
        return n * f(n - 1)

a = f(2023)
b = f(2020)
print(a / b)
