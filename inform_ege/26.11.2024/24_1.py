with open("24_1.txt") as f:
    s = f.readline()

s = s.replace("+", "*")
s = s.replace("**", "* *")
s = s.replace("*0", "* 0")

a = s.split()

for i in a:
    while len(i) and i[0] in "0*":
        i = 
