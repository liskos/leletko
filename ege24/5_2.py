import re
s = open("24data/k7-25.txt").read()
stroka = r"[C]+"  # сырая строка шаблон
pattern = re.compile(stroka) # скомпилированный шаблон
print(max([len(x.group()) for x in re.finditer(pattern, s)]))
