k = 0
for a in range(1001):
    if all( not((x < a +2) and (y < a -3) and (3*x + y > 66))  for x in range(1,1000) for y in range(1,1000)):
        print(a)
        k += 1

print(k)