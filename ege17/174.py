a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if x > 100 and int(str(x)[-2]) <= 4 and str(x)[-3] in "34567"]
print(len(b), min(b))