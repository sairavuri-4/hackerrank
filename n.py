if __name__ == '__main__':
    s=[]
    for _ in range(int(input())):
        s.append([input(),float(input())])
    g=sorted(set(i[1] for i in s))[1]
    for n in sorted(i[0] for i in s if i[1]==g):
        print(n)
