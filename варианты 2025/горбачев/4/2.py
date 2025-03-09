for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not (not (x or y) or w) or (not(z and (not (y and w))))
                print(x,y,z,w,"!", int(f))