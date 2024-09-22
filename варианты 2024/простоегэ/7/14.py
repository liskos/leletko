for x in "1234567":
    s = int(f"{x}1{x}", 16) + int(f"{x}3{x}3", 8)
    print(s, x)