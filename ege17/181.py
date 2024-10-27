a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if (str(x)[-1] == "5" or str(x)[-1] == "7") and x % 9 != 0 and x % 11 != 0]
print(len(b), max(b) + min(b))