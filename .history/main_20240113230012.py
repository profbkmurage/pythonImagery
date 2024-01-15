def get_choices():
    player = input('Enter your choice; paper rock or scissors: ')
    if player !='paper' and player !='scissors' and player !='rock':
        print ('you entered the wrong name')
    else:
        print (f'you chose {player}')


def computer_choice():
    choices = ['paper', 'rock', 'scissors']
    computer_selected = choices.random(choices)

get_choices()