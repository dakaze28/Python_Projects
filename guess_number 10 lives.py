import random
number=random.randrange(1,100)

def guess_the_number():
    print('This is a number\'s game. You have 10 chances to try and guess the number')
    guess=input("Guess the number between 1 and 100: ")
    lives = 10
    while True:
        try:
            int(guess)
            while int(guess)!=number and lives>0:
                if int(guess)>number:
                    print('Too high.')
                    lives=lives-1
                    print(f'You have {lives} chances left.')
                    if lives==0:
                        continue
                    guess=input("Guess the number between 1 and 100: ")
                if int(guess)<number and lives>-1:
                    print('Too low.')
                    lives=lives-1
                    print(f'You have {lives} chances left.')
                    if lives==0:
                        continue
                    guess=input("Guess the number between 1 and 100: ")
            if int(guess)==number and lives>0:
                print('Correct! You won!')
                print(f'You had {lives-1} more chance(s) left.') #El (-1) es para que te muestre los intentos adicionales que quedaban
                break
            if lives==0:
                print('Sorry, you ran out of chances. The correct answer was',number)
                break
        except ValueError: #Si coloca un tipo de dato diferente a entero, tira a error y no quita chances.
            print('The value isn\'t a number. Please try again.')
            guess=input("Guess the number between 1 and 100: ")
    

guess_the_number()