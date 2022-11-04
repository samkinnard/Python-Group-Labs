# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         SAM KINNARD
# Section:      565
# Assignment:   Lab 10.14
# Date:         1/11/2022

# function takes a new guess input in typical cases
def newguess():
    guess = input('What is your guess? ')
    return guess

# function takes input following atypical cases
def badinputguess():
    guess = input('Bad input! Try again: ')
    return guess

# game function that runs the while loop for guesses
# and contains a try except statement for bad guesses
def thegame():
    secretnumber = 26
    guesses = 0
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    a = newguess()
    while a != secretnumber:
        try:
            int(a)
        except ValueError:
            a = badinputguess()
            continue
        guesses += 1
        
        if int(a) < secretnumber:
            print('Too low!')
            a = newguess()
        elif int(a) > secretnumber:
            print('Too high!')
            a = newguess()
        else:
            break
    print(f'You guessed it! It took you {guesses} guesses.')
    
thegame()