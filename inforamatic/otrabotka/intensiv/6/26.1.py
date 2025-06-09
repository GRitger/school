with open("26-129.txt") as f:
    n = int(f.readline())
    a = []
    ind = 1
    beg = []
    end = []
    for i in f:
        x,y = [int(x) for x in i.split()]
        if x < y:
            beg.append([x,ind])
        else:
            end.append([y, ind])
        ind += 1
beg.sort()
end.sort(reverse=True)
print(beg[-1],end[0], len(beg)-1)



