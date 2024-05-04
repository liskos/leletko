for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not( not y or ( x == w)) and ( not z or x )
                if f:
                    print(x, y, z, w, "!", int(f))