for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = ( not x or y or z)  and (not x or not y or z ) and (  x or not y or not z)
            print(x,y,z,"|", int(f))