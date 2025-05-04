k = 0
for s in open("24data/24-s1.txt"):
    if s.count("S") == s.count("X"):
        k += 1

print(k)