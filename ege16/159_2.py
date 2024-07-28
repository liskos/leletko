s = set()
for i in range(1, int(18522000**0.5)+1):
    if 18522000 % i == 0:
        s.add(i)
        s.add(18522000 // i)
print(len(s))
print(sorted(s))