k = 0
for a in range(1,1000):
    if all( (not(x % 23 == 0) or (x%8!=0)) or (x%a==0) for x in range(1,1000)):
        k += 1
print(k)