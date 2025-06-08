for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((not z or x) and (not x or y)) or (w == (z or x))
                print(x,y,z,w,"!", int(f))