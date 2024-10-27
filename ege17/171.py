a = [int(x) for x in open("17data/17-4.txt")]
b = [x for x in a if (x % 31 == 0 or x % 47 == 0 or x % 53 == 0) and
     x % 3 == x % 5]
print(len(b), min(b))

