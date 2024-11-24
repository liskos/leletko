import sys
sys.stdin=open("24.txt")
s = input()
t = ""
m = 0
for i in s:
    if t == "" and i.isdigit() and i != "0":
        t = i
    elif t == "" and i == "0":
        t = ""
    elif t == "" and not i.isdigit():
        t = ""
    elif  t[-1] in "*+" and i == "0":
        t = ""
    elif t[-1].isdigit():
        t += i
    elif not t[-1].isdigit() and i.isdigit():
        t += i
    elif not t[-1].isdigit() and not i.isdigit():
        t = ""
    tt = t.replace("+", "*")
    if len(tt)>0 and tt[-1] == "*":
        tt = tt[:-1]
    tt = tt.split("*")
    x = len(tt)
    m = max(m, x)

print(m)
