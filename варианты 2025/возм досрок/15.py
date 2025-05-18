p = range(15,142+1)
q = range(38,167+1)
a1_best = 0
a2_best = 10000
for a1 in range(1000):
    for a2 in range(a1,1001):
        a = range(a1,a2+1)
        if all((not (x in q) or (not (not(x in a) and (x in p)) or (not (x in q)))) for x in range(1000)) and len(a) < a2_best-a1_best:
            a1_best = a1
            a2_best = a2

print(a2_best-a1_best)
