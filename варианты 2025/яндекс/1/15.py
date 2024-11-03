k = 10
p = range(64*k, 95*k+1)
q = range(72*k, 106*k+1)
d = 150
left = 0
right = 0
for a1 in range(95*k, 98*k):
    for a2 in range(105*k, 110*k):
        a = range(a1, a2+1)
        if all([not((x in q) and (x not in a)) or ((x in p) or (x not in q)) for x in range(150*k)]):
            if a2 - a1 < d:
                d = (a2 - a1)/k
                left = a1/k
                right = a2/k

print(d, left, right)