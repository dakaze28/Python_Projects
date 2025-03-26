import random

def rock_paper_scissor():
    pc_options=['r','p','s']
    pc_choice=random.choice(pc_options)
    rounds=[]
    while rounds.count('W')<3 and rounds.count('L')<3:
        user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
        if user_input=='score':
            print(rounds)
            user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
        if user_input=='q':
            
            print('Bye bye')
            break
        elif user_input not in pc_options:
            print('Chosen input is not an option, please choose again.') 
            user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
        elif user_input in pc_options:
            if user_input==pc_choice:
                print('It\'s a tie! Try again')
                pc_choice=random.choice(pc_options)
            elif user_input=='r':
                if pc_choice=='p': #user loses
                    print('You lose! Try again.')
                    pc_choice=random.choice(pc_options)
                    rounds.append('L')
                if pc_choice=='s': #user wins
                    print('You win! Congratulations!')
                    pc_choice=random.choice(pc_options)
                    rounds.append('W')
            elif user_input=='p':
                if pc_choice=='s': #user loses
                    print('You lose! Try again.')
                    pc_choice=random.choice(pc_options)
                    rounds.append('L')
                if pc_choice=='r': #user wins
                    print('You win! Congratulations!')
                    pc_choice=random.choice(pc_options)
                    rounds.append('W')
            elif user_input=='s':
                if pc_choice=='r': #user loses
                    print('You lose! Try again.')
                    pc_choice=random.choice(pc_options)
                    rounds.append('L')
                if pc_choice=='p': #user wins
                    print('You win! Congratulations!')
                    pc_choice=random.choice(pc_options)
                    rounds.append('W')
    print('This many rounds have passed:',rounds)
    if rounds.count('L')==3:                                        #Fuera del Loop de While (se ganó o perdió 3 rondas)
        print('You lost 3 times. Better luck next time!')
    else:
        print('Congratulations! You won',rounds.count('W'),'rounds.')

rock_paper_scissor()
