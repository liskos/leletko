for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            f = ( not a or b or not c ) and ( b or not c)
            print(a,b,c,"|", int(f))