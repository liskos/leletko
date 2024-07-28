def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 11 * n + f(n - 1)
    else:
        return  11 * f(n - 2) + n


a = 0
for i in range(35, 51):
    if f(i) % 2 == 0:
        a = a + f(i)
print(len(str(a)))