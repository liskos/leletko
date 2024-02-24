for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x or y) and ( not x or y or not z)
            print(x,y,z,"|", int(f))