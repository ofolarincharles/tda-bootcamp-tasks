#module to generate random number
import random
#a function to enclose the dice rolling simulator
def roll_dice():
    #prompt to ask if user will like to roll a dice
    prompt = str(input("Would you like to roll a dice?\n Hint! Answer YES or NO >>>"))
    #min=1 and max=6 
    dice = random.randint(1,6)
    #counter for while loop 
    counter = 0
    #ensuring it does not loop than once
    while counter < 1:
        #condition, message and action if user inputs YES/yes 
        if prompt == "YES" or prompt == "yes":
            return print("You rolled:", dice), roll_dice()
        #condition and message if user inputs NO/no
        elif prompt == "NO" or prompt == "no":
            return print("Bye, hope to see you again!")
        #condition, message and action if user inputs different from YES/yes , NO/no
        else:
            return print("Response not understood, Please answer YES or NO"), roll_dice()        
        counter+=1
#calling the dice rolling simulator
roll_dice()