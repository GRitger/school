def main():
    x = int(input())
    a = int(input())
    w = str(a)
    t = w[:-3]
    t += str(x) + w[-3:]
    print(t)

if __name__ == '__main__':
    main()