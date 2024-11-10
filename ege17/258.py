a = [int(x) for x in open("17data/17-257.txt")]
s = [x for x in a if x % 2 == 0]
t = [x for x in a if x % 2 != 0]
if max(s) > max(t):
    print(len(s), min(s))
else:
    print(len(t), min(t))
