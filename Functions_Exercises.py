#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
      for i in range(len(nums)):
            if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
                  return True
            else :
                  return False
nums=input('Enter numbers ')
print(arrayCheck(nums))

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(mystring):
  # CODE GOES HERE
  result=""
  for j in range(len(mystring)):
        if j%2==0:
              result=result+mystring[j]
  return result

mystring=input('Enter string ')
print(stringBits(mystring))
#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  # CODE GOES HERE
  a=a.lower()
  b=b.lower()
  return (b.endswith(a) or a.endswith(b))
a=input("Enter first word ") 
b=input("Enter second word ") 
print(end_other(a,b))
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(mystr):
  # CODE GOES HERE
  x=""
  for char in mystr:
    x+=char*2
  return x   
mystr=input("Enter text ")
print(doubleChar(mystr))
#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  # CODE GOES HERE
  return int(fix_teen(a)) + int(fix_teen(b)) + int(fix_teen(c))
def fix_teen(n):
  # CODE GOES HERE
  if n in   range(13,20) and n!=15 and n!=16:
        n=0
  return n
        
a=input("Enter number : ")
b=input("Enter number : ") 
c=input("Enter number : ")
print(no_teen_sum(a,b,c))
#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(num):
  # CODE GOES HERE
  k=0
  for element in  num:
        if int(element) % 2 == 0:
              k+=1
  return k
num=input("Enter number : ")
print(count_evens(num))