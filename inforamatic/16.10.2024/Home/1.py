from ipaddress import *

c = 0
m = 10**100
for ip in ip_network('110.159.76.0/255.255.255.128', False):
    one = f'{int(ip) : 32b}'
    print(one)
    '''if m > one.count("0"):
        m = one.count("0")
        print(one, one.count("0"))'''
    #m = min(one.count("0"), m)
#print(m)
#print(one)
