from random import randint
from math import sqrt

game_width = 10
game_height = 10

place_x = randint(0, game_width)
place_y = randint(0, game_height)
player_x = 0
player_y = 0
player_found_key = False
steps = 0
distance_before_move = sqrt((place_x-player_x)**2 + (place_y-place_y)**2)


while not player_found_key:
    steps += 1
    print()
    print('Możesz udać się w kierunkach okreslonych w/a/s/d')

    move = input('Dokąd idziesz?')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > game_height:
                print('uderzasz w sciane')
                player_y = game_height
        case 's':
            player_y -= 1
            if player_y < 0:
                print('uderzasz w sciane')
                player_y = 0

        case 'a':
            player_x -= 1
            if player_x < 0:
                print('uderzasz w sciane')
                player_x = 0
        case 'd':
            player_x += 1
            if player_x > game_width:
                print('uderzasz w sciane')
                player_x = game_width
        case 'q':
            quit()
        case ' _':
            print('nie wiem dokad idziesz')
            continue

    if place_x == player_x and place_y == player_y:
        print('znalazles kluczw w', steps, 'krokach!')
        break

    distance_after_move = sqrt((place_x-player_x)**2 + (place_y-place_y)**2)
    if distance_before_move > distance_after_move:
        print('zimniej')
    else:
        print('cieplej')

    distance_before_move = distance_after_move
