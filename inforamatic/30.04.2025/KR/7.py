from ipaddress import ip_network
n = 0
for ip in ip_network("156.132.15.138/255.255.252.0", False):
    if str(ip) == "156.132.15.138":
        print(n)
    n += 1