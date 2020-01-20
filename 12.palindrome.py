def palindrome():
    string=input("Enter the string to be checked : ")
    if string[::-1]==string:
        print("{0} is a palindrome".format(string))
    else :
        print("{0} is not a palindrome".format(string))
palindrome()