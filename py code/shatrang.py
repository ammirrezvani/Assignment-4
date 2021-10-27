def func(m,n):
    #m=int(input("enter m :"))
    #n=int(input("enter n :"))
    for i in range(m):
        for j in range(n):
            if i%2!=0 :
                print("#*",end="")
            else:
                print("*#",end="")
        print()
func(10,31)
