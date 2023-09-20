from symbols import LOGO, board_symbols, board_positions
import random
import time
import os

EMPTY_ROW = 12 * " "
WINNING_SYMBOL_NAMES = ["_horizontal_line", "_diagonal_nesw", "_vertical_line", "_diagonal_nwse"]
BOARD_LEFT_SIDE_SPACING = 7 * " "
INSTRUCTIONS_SPACING = 13 * " "
# Dictionary representing the position (key) and steps (values) for checking the rows,
# columns and diagonals for winners. The positions are represented by
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8
# For example, the 048 diagonal can be checked starting from 0 plus a step of 4
POS_STEP_WINNER_CHECK = {0: [1, 3, 4], 1: [3], 2: [2, 3], 3: [1], 6: [1]}


def clear_screen():
    os.system('cls')


def print_board(board_pos, winning_pos, get_symbols=True):
    board = return_symbols(board_pos, winning_pos) if get_symbols else board_pos
    for i in range(0, 9, 3):
        print(format_row(board[i], board[i + 1], board[i + 2]))
        if i != 6:
            print(BOARD_LEFT_SIDE_SPACING + 41 * "-")


def format_row(symbol1, symbol2, symbol3):
    row_strings = []
    symbol1_rows = split_symbol_rows(symbol1)
    symbol2_rows = split_symbol_rows(symbol2)
    symbol3_rows = split_symbol_rows(symbol3)
    for i in range(7):
        if i == 0 or i == 6:
            row_strings.append(BOARD_LEFT_SIDE_SPACING + EMPTY_ROW + "|" + EMPTY_ROW + " |" + EMPTY_ROW)
        else:
            row_strings.append(BOARD_LEFT_SIDE_SPACING + "".join(symbol1_rows[i - 1]) +
                               " | " + "".join(symbol2_rows[i - 1]) +
                               " | " + "".join(symbol3_rows[i - 1]) + " ")
    return "\n".join(row_strings)


def split_symbol_rows(symbol: str):
    return symbol.split("\n")


def return_symbols(board_pos, winning_pos):
    if winning_pos:
        first_num = winning_pos[0]
        second_num = winning_pos[1]
        symbol_name = WINNING_SYMBOL_NAMES[second_num - first_num - 1]
        return [board_symbols[board_pos[i]] if i not in winning_pos
                else board_symbols[f"{board_pos[i]}{symbol_name}"] for i in range(9)]
    return [board_symbols[symbol] for symbol in board_pos]


def print_logo():
    for line in LOGO:
        print(line)
    time.sleep(0.8)
    print_hash_line()


def print_hash_line():
    print("\n" + 55 * "#" + "\n")


def print_instructions():
    print(INSTRUCTIONS_SPACING + "Enter 'quit' to quit")
    print(INSTRUCTIONS_SPACING + "Enter 'restart' to restart")
    print(INSTRUCTIONS_SPACING + "For board positions, see below\n")
    number_symbols = [board_positions[key] for key in board_positions]
    print_board(number_symbols, None, get_symbols=False)
    time.sleep(0.8)
    print_hash_line()


class Game:
    def __init__(self):
        self.is_running = True
        self.board = []
        self.current_player = "x"
        self.starting_player()
        self.restart_board()

    def starting_player(self):
        self.current_player = random.choice(["x", "o"])

    def restart_board(self):
        self.board = ["_" for _ in range(9)]

    def change_player(self):
        self.current_player = "o" if self.current_player == "x" else "x"

    def add_symbol(self, pos):
        self.board[pos] = self.current_player

    def reset_game(self):
        self.starting_player()
        self.restart_board()

    def check_winner(self):
        for key, value in POS_STEP_WINNER_CHECK.items():
            winning_pos = self.check_pos(key, *value)
            if winning_pos:
                return winning_pos

    def is_draw(self):
        return "_" not in self.board

    def check_pos(self, *args):
        pos = args[0]
        for i in range(1, len(args)):
            step = args[i]
            stop = pos + 2 * step
            symbol1, symbol2, symbol3 = self.board[pos:stop + 1:step]
            if symbol1 != "_" and symbol1 == symbol2 and symbol1 == symbol3:
                return [pos + i * step for i in range(3)]
        return None

    def end_game(self):
        self.is_running = False


def main():
    clear_screen()
    print_logo()
    print_instructions()
    game = Game()
    while game.is_running:
        pos = input(f"{game.current_player.upper()} Player, please enter a position (1-9) to make your move: ")
        if pos.lower() == "quit":
            print("Bye!")
            game.end_game()
        elif pos.lower() == "restart":
            main()
        else:
            try:
                pos = int(pos)
                if pos < 1 or pos > 9:
                    raise ValueError
            except ValueError:
                print("\nInvalid position or command, please try again.")
            else:
                pos -= 1
                if game.board[pos] != "_":
                    print("\nThis position is already occupied, please choose a valid one.")
                else:
                    game.add_symbol(pos)
                    winning_pos = game.check_winner()
                    print()
                    print_board(game.board, winning_pos)
                    if winning_pos or game.is_draw():
                        if winning_pos:
                            print(f"{game.current_player.upper()} Player is the winner!")
                        else:
                            print("It is a draw!")
                        play_again = input("Do you wish to play again? ('Yes' to play again): ")
                        if play_again.lower() == "yes":
                            clear_screen()
                            print_instructions()
                            game.reset_game()
                        else:
                            game.end_game()
                            print("Bye!")
                    else:
                        game.change_player()
            print_hash_line()


main()
