file = open("44t.txt")
n = int(file.readline())
a = [int(x) for x in file]
b = [[(x-1)//500+1,x] for x in a]
print(n)
print(b)
