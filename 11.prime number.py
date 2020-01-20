def prime():
    x=int(input("Enter number to be checked"))
    for i in range(2,int(x/2)):
        if x % i ==0:
            c=1
        else:
            c=0
    if c==0:
        print("{} is a prime number".format(x))
    else :
        print(f"{x} is not a prime number ")
prime()
