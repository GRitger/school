with open("26-145.txt") as f:
    a = []
    b = []
    vagon, mest = [int(x) for x in f.readline().split() ]
    for i in f:
        if i != "\n":
            vz, children = [int(x) for x in i.split() ]
            if vz + children > 2:
                a.append([vz,children])
            else:
                b.append([vz, children])
a.sort(key=lambda x :(x[0], x[1]))
b.sort(key=lambda x :(x[0], x[1]))

arr = [[mest, mest]*vagon]
print(arr)