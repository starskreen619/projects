from random import randint
import os


class Ship:
    def __init__(self, position, health):
        self.position = position
        self.health = health
        self.size = 1

    # def afloat(self)


# Ship1 = Ship(board_display[2, 2], 1)
# Ship2 = Ship([3, 3], 1)
# Ship3 = Ship([1, 1], 1)

# row_size = abs(eval(input('Enter row size: ')))
# col_size = abs(eval(input('Enter colunm size: ')))
row_size = 5  # number of rows
col_size = 5  # number of columns
num_ships = 3
num_guesses = 5

ship_list = []
board = [[0] * col_size for x in range(row_size)]
# board_display = [{"O": True} * col_size for x in range(row_size)]
board_display = [["O"] * col_size for x in range(row_size)]

Ship1 = Ship(board_display[2, 2], 1)
Ship2 = Ship([3, 3], 1)
Ship3 = Ship([1, 1], 1)


def print_board(board_array):
    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
    for r in range(row_size):
        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))


# for turn in range(num_guesses):
#     print("Turn:", turn + 1, "of", num_guesses)
#     print("Ships left:", len(ship_list))
#     print()

#     guess_coords = {}
#     while True:
#         guess_coords['row'] = get_row()
#         guess_coords['col'] = get_col()
#         if board_display[guess_coords['row']][guess_coords['col']] == 'X' or \
#                 board_display[guess_coords['row']][guess_coords['col']] == '*':
#             print("\nYou guessed that one already.")
#         else:
#             break


def drop_bomb():

    board_display[guess1-1][guess2-1] = "X"
    # ship_hit = False
    # for ship in ship_list:
    #     if ship.contains(guess_coords):
    #         print("Hit!")
    #         ship_hit = True
    #         board_display[guess_coords['row']][guess_coords['col']] = 'X'
    #         if ship.destroyed():
    #             print("Ship Destroyed!")
    #             ship_list.remove(ship)
    #         break
    # if not ship_hit:
    #     board_display[guess_coords['row']][guess_coords['col']] = '*'
    #     print("You missed!")

    # print_board(board_display)

    # if not ship_list:


while True:
    guess1 = int(input("Row Guess: "))
    guess2 = int(input("Column Guess: "))
    drop_bomb()
    print_board(board_display)
