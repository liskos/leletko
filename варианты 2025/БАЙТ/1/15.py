p = range(15,30+1)
q = range(60,80+1)
a1_best = 0
a2_best = 0
for a1 in range(100):
    for a2 in range(a1,100):
        a = range(a1,a2+1)
        if a2-a1 > a2_best - a1_best and all(  not (not(not(x in a) or (x in p))) or (not (not(x in a) or (not(x in q)))) for x in range(100)):
            a1_best = a1
            a2_best = a2

print(a1_best,a2_best, a2_best-a1_best)
