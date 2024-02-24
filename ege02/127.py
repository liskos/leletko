for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = (a or not c )  and ( b or c)
            print(a,b,c,"|", int(f))