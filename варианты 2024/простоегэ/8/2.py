for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not(not y or w) or ( not x or z ) or ( not x )
                print(x, y, z, w, "!", int(f))