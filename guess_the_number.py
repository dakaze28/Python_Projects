import random
number=random.randrange(1,100)

def guess_the_number():
    guess=input("Guess the number between 1 and 100: ")
    while (True):
        try:
            int(guess)
            while int(guess)!=number:
                if int(guess)>number:
                    print('Too high.')
                    guess=input("Guess the number between 1 and 100: ")
                if int(guess)<number:
                    print('Too low.')
                    guess=input("Guess the number between 1 and 100: ")
            else:
                print('Correct! You won!')
                break
        except ValueError:
            print('The value isn\'t a number. Please try again.')
            guess=input("Guess the number between 1 and 100: ")
            

guess_the_number()