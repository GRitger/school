def fu(cl):
    ans = [0,0]
    rast = 10000000000000000000000000000000000000000000000000000000000000000000000000000
    for i in cl:
        x, y = i
        s = 0
        for j in cl:
            x2, y2 = j
            s += ((x-x2)**2 + (y-y2)**2)**0.5
        if s < rast:
            rast = s
            ans = i
    return ans
