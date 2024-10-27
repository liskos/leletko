a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if x % 3 == 0 and x % 9 != 0 and int(str(x)[-1]) >= 4]
print(len(b), sum(b)//len(b))
