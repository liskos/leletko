p = range(3, 83+1)
q = range(62, 131+1)
a1_best = 0
a2_best = 1000
for a1 in range(1, 200):
    for a2 in range(a1, 200):
        a = range(a1, a2 + 1)
        if a2 - a1 < a2_best - a1_best and all([not (not(x in q)) or (not(not(x in a) and (x in p)) or (x in q)) for x in range(1, 200)]):
            a1_best = a1
            a2_best = a2
print(a1_best, a2_best, a2_best-a1_best)

k =10
p = range(3*k, 83*k+1)
q = range(62*k, 131*k+1)
a1_best = 0
a2_best = 1000
for a1 in range(1*k, 10*k):
    for a2 in range(55*k, 65*k):
        a = range(a1, a2 + 1)
        if a2 - a1 < a2_best - a1_best and all([not (not(x in q)) or (not(not(x in a) and (x in p)) or (x in q)) for x in range(1, 200*k)]):
            a1_best = a1
            a2_best = a2
print(a1_best, a2_best, (a2_best-a1_best)/k)