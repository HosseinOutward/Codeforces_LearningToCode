for i in range(int(input())):
    l=input()
    if len(l)>10:
        print(l[0]+str(len(l)-2)+l[-1])
    else:
        print(l)