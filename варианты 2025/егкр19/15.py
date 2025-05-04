b = range(36,75+1)
c = range(60,110+1)
b_a1 = 0
b_a2 = 10000
for a1 in range(1000):
    for a2 in range(a1,1000):
        a = range(a1,a2+1)
        if a2 - a1 < b_a2-b_a1 and all( not(not( x in a)) or ((x in b) == (x in c)) for x in range(1000)):
            b_a1 = a1
            b_a2 = a2

print(b_a2-b_a1)
print(b_a1)
print(b_a2)
