from random import randint

options = ['rock', 'paper', 'scissors']


def start_game(options):
    random = ''
    for _ in range(0, len(options)):
        random = options[randint(0, 2)]
    print('Choose Rock, Paper or Scissors')
    choose = input('What would you choose?: ')
    print(choose)
    print(options)
    if choose in options:
        if choose == 'rock' and random == 'paper':
            print('Computer choose paper, you lose!')
        elif choose == 'paper' and random == 'scissors':
            print('Computer choose scissors, you lose!')
        elif choose == 'scissors' and random == 'rock':
            print('Computer choose rock, you lose!')
        elif choose == random:
            print('It\'s a drow!')
        else:
            print('Congratulations! You win this game! Computer choose', random)
    else:
        print('Invalid option, please choose Rock, Paper, or Scissors')
    print('Do you want to play again?')
    option = input('yes/no?: ')
    print(option)
    if option == 'yes':
        return start_game(options)


start_game(options)
