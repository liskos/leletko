a = [int(x) for x in open("17data/17-6.txt")]
r = []
k = 0
for i in range(len(a) -2):
    if bin(a[i]).count("1") == 3 and bin(a[i+1]).count("1") == 3 and bin(a[i+2]).count("1") == 3 :
        r.append(max(a[i], a[i+1], a[i+2]))
print(len(r), sum(r))