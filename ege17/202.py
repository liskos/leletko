a = [int(x) for x in open("17data/17-202.txt")]
b = []
def f(x):
    return len(str(abs(x))) == 3 and x > 0 and abs(x) % 10 == 5

for i in range(len(a)- 2):
    if not f(a[i]) and f(a[i +1 ]) and not f(a[i + 2]):
        b.append(sum(a[i:i + 3]))

print(len(b), max(b))