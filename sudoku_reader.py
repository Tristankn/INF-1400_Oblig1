import time
start_time = time.time()

class Sudoku_reader:

    def __init__(self, filename):
        self.file = open(filename, "r")
        self.current_line = 0

    # returnerer en 9x9 2D liste av heltall
    def next_board(self):
        try:
            board_txt = self.file.readline()
            board = [[0 for _ in range(9)] for _ in range(9)]
            sym_num = 0
            for i in range(9):
                for j in range(9):
                    board[i][j] = int(board_txt[sym_num])
                    sym_num += 1
            return board
        except:
            print("Reading error, no more sudokus to solve!")
            print("Solving the sudokus took %s seconds!" % (time.time() - start_time))
            quit(-1)

