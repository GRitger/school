from ipaddress import ip_network
k = 0
for ip in ip_network('94.149.96.0/255.255.224.0', 0):
    p = f'{int(ip):032b}'
    if p.count('1')%3==0 and p[-2:]=='11':
        k+=1
        print(p)

print(k)