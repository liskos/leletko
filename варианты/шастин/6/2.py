for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or ((not z) and w ) or w) == ( y and (not x ) and w )
                print(x, y, z, w, "!", int(f))
