def f( n ):
  global a
  a += 1
  if n >= 1:
    a += 1
    f(n-1)
    f(n//3)
    a += 1

a = 0
f(280)
print(a)