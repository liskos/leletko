k = 10
c = range(48*k,94*k+1)
j = range(83*k,100*k+1)
x1, x2 = 0,0
l = 0
for a1 in range(45*k,50*k):
    for a2 in range(95*k,110*k):
        a = range(a1,a2+1)
        if all([ ((x in c) or (x in j)) or (x not in a) for x in range(1, 1000*k)]):
            if a2 - a1 > l:
                l = a2 - a1
                x1 = a1
                x2 = a2
print(x1/k,x2/k,l/k)
