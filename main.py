import pprint


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("---------")
            for j in range(len(bo)):
                if j % 3 == 0:
                    print(" | ", end="")
                if j == 8:
                    print(bo[i][j], end="\n")
                else:
                    print(str(bo[i][j]) + " ", end="")


if __name__ == '__main__':
    board = [
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
    printer.pprint(board)
