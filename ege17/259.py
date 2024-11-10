a = [int(x) for x in open("17data/17-257.txt")]
s = [x for x in a if x % 11 == 0]
t = [x for x in a if x % 17 == 0]
if len(s) > len(t):
    print(len(s), min(s))
else:
    print(len(t), max(t))
