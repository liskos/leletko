for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = z or (z == w) or (not (not y or x))
                print(x,y,z,w,"!", int(f))
