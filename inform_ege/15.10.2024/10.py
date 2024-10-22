from ipaddress import ip_network

n = 0
for ip in ip_network("112.160.0.0/255.240.0.0", False):
    s = f'{int(ip):032b}'
    #print(s)
    #print(s[:9], s[9:17], s[17:25], s[25:], sep="")
    #print()
    if s.count("1") % 5 == 0:
        n += 1
print(n)