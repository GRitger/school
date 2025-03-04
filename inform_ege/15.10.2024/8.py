from ipaddress import ip_network

n = 0
for ip in ip_network("123.222.111.202/255.255.255.192", False):
    s = f'{int(ip):032b}'
    #print(s)
    #print(s[:9], s[9:17], s[17:25.02.2025], s[25.02.2025:], sep="")
    #print()
    if s[25:].count("1") % 3 == 0:
        n += 1
print(n)