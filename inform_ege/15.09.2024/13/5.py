from ipaddress import *

c = 0
for ip in ip_network('123.222.111.192/255.255.255.192', False):
    one = f'{int(ip) : 32b}'[24:]
    if one.count("1") % 3:
        c += 1
print(c)
