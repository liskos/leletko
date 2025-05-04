k = 0
for s in open("24data/24-s1.txt"):
    if s.count("J") > s.count("E"):
        k+=1

print(k)