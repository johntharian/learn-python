###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

import random
def get_guess():
    return list(input("What is your guess? "))

def generate_random():
    digits=[str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,guess):
    if guess ==code:
        return "Code Correct"
    clues=[]
    for ind,num in enumerate(guess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")
    if clues==[]:
       return ["Nope"]  
    else :
        return clues   


    

while generate_clues!="Code Correct":
    x=get_guess()
    r=generate_random()
    report=generate_clues(r,x)
    print("Here is the result: ")
    for element in report:
        print(element)