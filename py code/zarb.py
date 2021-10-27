def func(m,n):
    #m=int(input("enter m :"))
    #n=int(input("enter n :"))
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(i*j,end=" ")
        print()
func(10,15)
