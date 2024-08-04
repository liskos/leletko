
a = 0
for i in range(10**8, 2*10**8+1):
    if i % 3 !=0 and i % 5 != 0:
        a += 1
print(a)