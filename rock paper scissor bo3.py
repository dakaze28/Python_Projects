import random

def rock_paper_scissor():
    pc_options=['r','p','s']
    pc_choice=random.choice(pc_options)
    rounds=[]
    user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
    while len(rounds)<4:
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
                tie=True
                print('It\'s a tie! Try again')
                pc_choice=random.choice(pc_options)
                user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
            elif user_input=='r':
                if pc_choice=='p': #user loses
                    print('You lose! Try again.')
                    pc_choice=random.choice(pc_options)
                    rounds.append('L')
                    user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
                    tie=False
                if pc_choice=='s': #user wins
                    print('You win! Congratulations!')
                    pc_choice=random.choice(pc_options)
                    rounds.append('W')
                    user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
                    tie=False
            elif user_input=='p':
                if pc_choice=='s': #user loses
                    print('You lose! Try again.')
                    pc_choice=random.choice(pc_options)
                    rounds.append('L')
                    user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
                    tie=False
                if pc_choice=='r': #user wins
                    print('You win! Congratulations!')
                    pc_choice=random.choice(pc_options)
                    rounds.append('W')
                    user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
                    tie=False
            elif user_input=='s':
                if pc_choice=='r': #user loses
                    print('You lose! Try again.')
                    pc_choice=random.choice(pc_options)
                    rounds.append('L')
                    user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
                    tie=False
                if pc_choice=='p': #user wins
                    print('You win! Congratulations!')
                    pc_choice=random.choice(pc_options)
                    rounds.append('W')
                    user_input=input('Choose between rock (r), paper(p) or scissor(s): ')
                    tie=False

rock_paper_scissor()

#Best of 3: tiene una lista de rounds (cuando haya 2 elementos Y o N en una lista creada, se declara ganador)