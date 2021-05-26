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
            # Checks the 3 X 3 box, row and column
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


# backtracing code... not mine
def solve_backtracing(board):
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True
    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i
            if solve_backtracing(board):
                return True
            board[row][col] = 0
    return False


# backtracing code... not mine
def valid(board, pos, num):
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != 1:
            return False
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)


if __name__ == '__main__':
    game = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    printer = pprint.PrettyPrinter(width=41, compact=True)
    solve_backtracing(game)
    printer.pprint(game)
    print(is_solved(game))
    game[0][0] = 2
    print(is_solved(game))