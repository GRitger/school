from ipaddress import ip_network
n =0
for ip in ip_network('123.222.111.192/255.255.255.248', False):
    if f'{int(ip):032b}'[24:].count("0") %3 :
        n+=1
print(n)
