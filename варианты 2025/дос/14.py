import string
t = "0123456789abcdefghijk"
for x in t:
    a = int(f"82934{x}2",21) + int(f"2924{x}{x}7",21) + int(f"67564{x}8", 21)
    if a % 20 == 0:
        print(a//20)
        break