import sys
sys.stdin=open("24.txt")
s = input()
t = ""
m = 0
for i in s:
    if (t == "") and (i in "*+"):
        t = ""
    elif (t == "") and (i in "789"):
        t = i
    elif (t[-1] == "+") and (i in "789"):
        t += i
    elif (t[-1] == "+") and (i in "+*"):
        t = ""
    elif (t[-1] in "789") and (i in "+789"):
        t += i
    elif (t[-1] in "789") and (i in "*"):
        t = ""
    if t and t[-1] != "+":
        m = max(m, eval(t))
print(m)