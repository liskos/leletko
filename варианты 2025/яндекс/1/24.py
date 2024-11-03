import functools
@functools.lru_cache(None)
def f(s):
    if len(s)==0:
        return 0
    if "*" not in s and "+" not in s:
        if int(s) == 0:
            return 1
        else:
            return 0
    if eval(s) == 0:
        return len(s)
    sleft = s
    while (sleft[0] not in "*+")  and len(sleft)>0:
        sleft = sleft[1:]
    sleft = sleft[1:]
    sright = s
    while sright[-1] not in "*+" and len(sright) > 0:
        sright = sright[:-1]
    sright = sright[:-1]
    return max(f(sleft), f(sright))



import sys
sys.stdin = open("24.txt")
s = input()
s = s.replace("++", " ")
s = s.replace("**", " ")
s = s.replace("+*", " ")
s = s.replace("*+", " ")
s = s.replace(" +", " ")
s = s.replace(" *", " ")
s = s.replace("+ ", " ")
s = s.replace("* ", " ")
a = sorted(s.split(), key=len, reverse=True)
a = [x for x in a if len(x) >= 167]
z = 0
for i in a:
    z = max(z, f(i))
    print(z)
