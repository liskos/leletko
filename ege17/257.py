a = [int(x) for x in open("17data/17-257.txt")]
s = [x for x in a if x % 7 == 0]
t = [x for x in a if x % 13 == 0]
if min(s) > min(t):
    print(len(s), max(s))
else:
    print(len(t), max(t))
print(len(a))