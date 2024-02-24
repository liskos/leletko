for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a and not c ) or ( not b and not c)
            print(a,b,c,"|", int(f))