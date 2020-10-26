from random import randint
import os


class Ship:
    def __init__(self, position, health):
        self.position = position
        self.health = health
        self.size = 1


row_size = abs(eval(input('Enter row size: ')))
col_size = abs(eval(input('Enter colunm size: ')))
# row_size = 5  # number of rows test
# col_size = 5  # number of columns test
num_guesses = 5

ship1x = randint(1, row_size)
ship1y = randint(1, col_size)
Ship1 = Ship([ship1x, ship1y], 1)

ship2x = randint(1, row_size)
ship2y = randint(1, col_size)
Ship2 = Ship([ship2x, ship2y], 1)

ship3x = randint(1, row_size)
ship3y = randint(1, col_size)
Ship3 = Ship([ship3x, ship3y], 1)

print(ship1x, ship1y)  # test print
# print(ship2x, ship2y)   test print
# print(ship3x, ship3y)   test print

ship_list = []
# board = [[0] * col_size for x in range(row_size)]
board_display = [["O"] * col_size for x in range(row_size)]


def print_board(board_array):
    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
    for r in range(row_size):
        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))


def drop_bomb(guess1, guess2):
    global num_ships
    num_ships = 3
    while num_ships > 0:
        if guess1 == ship1x and guess2 == ship1y:
            print("Hit!!! Ship 1 Sunked!!!")
            board_display[guess1-1][guess2-1] = "X"
            num_ships -= 1
            # print(f"You have {num_ships} ships left!")
        elif guess1 == ship2x and guess2 == ship2y:
            print("Hit!!! Ship 2 Sunked!!!")
            board_display[guess1-1][guess2-1] = "X"
            num_ships -= 1
            # print(f"You have {num_ships} ships left!")
        elif guess1 == ship3x and guess2 == ship3y:
            print("Hit!!! Ship 3 Sunked!!!")
            board_display[guess1-1][guess2-1] = "X"
            num_ships -= 1
            # print(f"You have {num_ships} ships left!")
        else:
            print("\nMiss!!!")
            board_display[guess1-1][guess2-1] = "*"
            break


while num_guesses > 0:
    guess1 = int(input("Row Guess: "))
    guess2 = int(input("Column Guess: "))
    drop_bomb(guess1, guess2)
    print_board(board_display)
    num_guesses -= 1
else:
    print("You lose! Thank you for playing")
