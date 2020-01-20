
def  armstrong():
    x=input("Enter number to be checked : ")
    y=x
    summ=0
    cube=0
    i=len(x)
    j=len(x)
    while i > 0:
        cube=(int(x)%10)**int(j)
        summ=summ + cube
        x=int(x) // 10
        i-=1
    if int(summ)==int(y):
        print(" The entered number is an armstrong number")
    else :
        print("The entered number is not an armstrong number")
    print(summ)    
armstrong()