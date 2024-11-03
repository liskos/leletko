def f(n):
    if str(n).count("9") >= 1:
        return 1
    else:
        return 0


a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 2):
    if (a[i] < sr or a[i+1] < sr or a[i+2] < sr) and ((f(a[i]) + f(a[i+1]) + f(a[i+2])) == 3):
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))