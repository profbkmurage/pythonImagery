def get_choices():
    player = input('Enter your choice; paper rock or scissors: ')
    if player !='paper' and player !='scissors' and player !='rock':
        print ('you entered the wrong name')
    else:
        return f'you chose {player}'