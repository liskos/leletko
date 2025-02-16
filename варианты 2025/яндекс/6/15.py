b = {-42, -10,-8,2,16}
c = {-10, -4, 2, 15, 23}
a = set()
for i in range(0,100):
    a.add(i)
    if not all((not (x in a) or (x in b) or (x in c)) for x in range(-100,100)):
        a.remove(i)
print(sum(a))