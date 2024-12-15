k = 10
p = range(32*k,55*k+1)
q = range(40*k, 79*k+1)
m1 = 0
m2 = 0
l = 100*k
for a1 in range(30*k,35*k):
    for a2 in range(50*k, 60*k):
        a = range(a1,a2+1)
        if all(not((x not in q) or (x not in a)) or ((x in a)==(x in p)) for x in range(0*k, 100*k)):
            if a2-a1 < l:
                m1 = a1
                m2 = a2
                l = a2-a1
print(m1/k,m2/k, l/k)