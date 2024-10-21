from ipaddress import *

c = 0
for ip in ip_network('123.206.97.128/255.255.255.224', False):
    one = f'{int(ip) : 32b}'
    if one[-3:] == "101" or one[-3:] == "010":
        c += 1
print(c)
