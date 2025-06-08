import string
i = "0123456789ABCD"
for x in i:
    a = int(f"4b3{x}1c7", 14) + int(f"5{x}g83f7", 17)
    if a % 15 == 0:
        print(a//15)
        break