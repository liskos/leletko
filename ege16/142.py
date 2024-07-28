def f(n):
    if str(n ** 0.5) == str(int(n ** 0.5)) + ".0":
        return n ** 0.5
    else:
        return  f(n + 1) + 1

print(f( 4850) + f(5000))