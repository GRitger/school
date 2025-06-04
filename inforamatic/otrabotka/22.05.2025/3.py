def p(x:int):
    d = 2
    while d *d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def d(x:int):
    a = []
    d = 2
    while d *d < x:
        if x % d == 0:
            if p(d):
                pass