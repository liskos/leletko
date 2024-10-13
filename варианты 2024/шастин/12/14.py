for x in "0123456789ABCDEFGHIJKL":
    s = int(f"56{x}c20", 22) + int(f"89F{x}2", 22) + int(f"h24{x}k21", 22)
    if s % 21 == 0:
        print(s // 21)