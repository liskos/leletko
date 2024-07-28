import functools
@functools.lru_cache(1000000)
def f(n, a):
    if n == 0:
        return 1
    if a == 3:  # если глубина погружения 4, то дальше не считай, нет смысла, уже больше 3
        return 1
    if n % 2 != 0:
        return 1 + f(n - 1, a+1) # если прибавляет 1 к значению, то а увеличиваем на 1
    return f(n // 2, a)   # тут функция не изменяется, значит и а мы не увеличиваем



a = 252
for i in range(6*10**6, 500000000+1):
    if f(i, 0) == 3:
        a = a + 1
    if i % 1000000 == 0:
        print(i, a)
print(a)