def f(s):
    while ("01" in s) or ("02" in s) or ("03" in s):
        s = s.replace("01", "30", 1)
        s = s.replace("02", "3103", 1)
        s = s.replace("03", "1201", 1)
    return s
