p = range(44,49+1)
q = range(28,53+1)
a1_best = 0
a2_best = 0
for a1 in range(100):
    for a2 in range(a1,100):
        a = range(a1,a2+1)
        if a2-a1 > a2_best - a1_best and all( (not(x in a) or (x in p)) or (x in q) for x in range(100)):
            a1_best = a1
            a2_best = a2

print(a1_best,a2_best, a2_best-a1_best)

k = 10
p = range(44*k,49*k+1)
q = range(28*k,53*k+1)
a1_best = 0
a2_best = 0
for a1 in range(25*k,30*k):
    for a2 in range(50*k,55*k):
        a = range(a1,a2+1)
        if a2-a1 > a2_best - a1_best and all( (not(x in a) or (x in p)) or (x in q) for x in range(100*k)):
            a1_best = a1
            a2_best = a2

print(a1_best/k,a2_best/k, (a2_best-a1_best)/k)