from ipaddress import *

c = 0
for ip in ip_network('153.24.165.32/255.255.255.224', False):
    one = f'{int(ip) : 32b}'
    if one[:9].count("1") + one[9:17].count("1") < one[17:25].count("1") + one[25:].count("1"):
        c += 1
print(c)
