from ipaddress import ip_network
n = 0
for A in range(0, 256):
    f =True
    for ip in ip_network(f"196.233.{A}.52/255.255.255.240", False):
        st = f'{int(ip):32b}'
        if st[:16].count("1") > st[16:].count("1"):
            f = False
    if f :
        print(A)



#ans: 192 or