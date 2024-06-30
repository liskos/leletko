def f( n ):
  a.append(n-5)
  if n > 1:
    a.append(n+8)
    f(n-2)
    f(n-3)



for n in range(1, 1000):
    a = []
    f(n)
    if sum(a) > 3200000:
        print(n, sum(a))
        break