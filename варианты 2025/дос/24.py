import re
s = open("24_21421.txt").read()
pattern = r"([1-9AB][0-9AB]+[02468A])"
m = [ x.group() for x in re.finditer(pattern,s)]
r = max(m,key=len)
print(r, len(r))