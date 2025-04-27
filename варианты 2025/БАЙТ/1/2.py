for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not (not y or x) and (not(not w and z)) and (not (x and w))
                print(x,y,z,w, "!", int(f))