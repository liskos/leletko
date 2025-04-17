import re
s = open("24.txt").read()
number = r"([1-9AB]+)"
virag = rf"{number}([+*-]{number})*"
r = [len(x.group()) for x in re.finditer(virag, s)]
print(max(r))