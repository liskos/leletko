
a = [int(x) for x in open("17.txt")]
sr = sum(a)/ len(a)
r = []
for i in range(len(a)-1):
    if abs(a[i] + a[i+1]) > sr:
        r.append(a[i]+a[i+1])
print(len(r), min(r))