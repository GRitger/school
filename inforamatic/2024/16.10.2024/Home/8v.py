from ipaddress import *

c = 0
for ip in ip_network('86.65.32.0/255.255.224.0', False):
    one = f'{int(ip) : 32b}'
    if one.count("1") == one.count("0"):
        c += 1
print(c)
# решать математикой
