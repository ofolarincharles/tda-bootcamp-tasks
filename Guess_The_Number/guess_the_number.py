#module to generate random number
import random
#a random number meant to be guessed between 0 and 100
number = random.randint(0,100)
#funtion to wrap my codes
def guess_a_number():
    #counter set at default zero attempts
    counter=0
    #loop ensuring maximum of three attempts
    while counter<3:
        #input prompt to take guesses
        guess = int(input("Guess a number guess from 0 and 100>>>"))
        #if, elif and else block for conditions and message to display for each attempt
        if number==guess:
            print("Your guess is:",guess,"\nYou must be a genius! You guessed the number correctly")
            break
        elif number < guess:
            print("Your guess is:",guess,"\nOops! Nice try, your guess is higher and wrong")
        elif number > guess:
            print("Your guess is:",guess,"\nOops! Nice try, your guess is lower and wrong")
        else:
            print("Oops! Invalid entry, Enter a number between 0 and 100")
        #add to counter after each attempt
        counter+=1
    #final prompt to user after the three attempts    
    return print("\nThree attempts exhausted for today, try again tommorow, The correct number is:", number)
#to call my function
guess_a_number()