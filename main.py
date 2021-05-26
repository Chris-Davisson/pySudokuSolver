import pprint
import numpy


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("---------")
            for j in range(len(board)):
                if j % 3 == 0:
                    print(" | ", end="")
                if j == 8:
                    print(board[i][j], end="\n")
                else:
                    print(str(board[i][j]) + " ", end="")


def is_solved(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            # Checks for empty, if it is then it can't be solved
            if board[i][j] > 9 or board[i][j] < 1:
                return False
            if not check_box(board, i, j) and not check_array(board[i]) and not check_array(column(board, j)):
                return False
    return True


def check_array(row):
    for i in row:
        if i == 0:
            return False
        count = 0
        for j in range(0, len(row)):
            if row[j] == i:
                count += 1
            if count > 1:
                return False
    return True


def check_box(board, x, y):
    row = x // 3
    col = y // 3
    box_array = []
    for i in range(0, 3):
        for j in range(0, 3):
            box_array.append(board[row * 3 + i][col * 3 + j])
    return check_array(box_array)


def column(board, i):
    return [row[i] for row in board]


if __name__ == '__main__':
    game = [
        [1, 2, 3, 1, 1, 0, 0, 0, 0],
        [4, 5, 6, 0, 0, 0, 0, 0, 0],
        [7, 8, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    printer = pprint.PrettyPrinter(width=41, compact=True)
    printer.pprint(game)

    print(is_solved(game))
