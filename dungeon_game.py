import random
import os


CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4),
    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6),
]


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    # get player location
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    return x, y


def get_moves(player):
    moves = ["UP", "DOWN", "LEFT", "RIGHT"]
    x, y = player
    # if player y == 0 they can't go up
    if y == 0:
        moves.remove("UP")
    # if player y == 6 they can't go down
    if y == 6:
        moves.remove("DOWN")
    # if player x == 0 they can't go left
    if x == 0:
        moves.remove("LEFT")
    # if player x == 6 they can't go right
    if x == 6:
        moves.remove("RIGHT")
    
    return moves


def print_board(player, monster, door):
    print('_'*6)
    tile = '|{}'
    for cell in CELLS:
        x, y = cell
        if x < 6:
            line_end = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def game_loop():
    clear_screen()
    playing = True
    player, monster, door = get_locations()
    while playing:
        print_board(player, monster, door)
        moves = get_moves(player)

        print("You're currently in room {}.".format(player))
        print("You can move {}.".format(", ".join(moves)))
        print("Enter QUIT to quit.")

        move = input("> ").upper()
        clear_screen()

        if move == 'QUIT':
            break
        if move in moves:
            player = move_player(player, move)
            if player == monster:
                print('You died!\n')
                playing = False
            elif player == door:
                print('You escaped!\n')
                playing = False
            else:
                continue
        else:
            input('You cannot move there!')
            clear_screen()
    else:
        if input('Play again? [Y/n]').lower() != 'n':
            game_loop()


print("Welcome to the dungeon!")
input("Press ENTER to begin!")
clear_screen()
game_loop()
print("Thanks for playing!")
