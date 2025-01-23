from sudoku_reader import Sudoku_reader

class Board:
    # It is your task to subclass this in order to make it more fit
    # to be a sudoku board

    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.rawnums = nums
        self.nums = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]

    def _set_up_nums(self):
        # Denne funksjonen må hente tall fra sudokureader og putte dem inn i stedet for None
        
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                self.nums[i][j] = Square(i, j, self.rawnums[i][j])

            
    def _set_up_elems(self, squareboard):
        
        x = []
        y = []
    
        for b_row in squareboard:
            for b_column in b_row:




        
        

    def solve(self):
        # Your solving algorithm goes here!
        pass

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        r += "[["
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + ", "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r

class SudokuBoard(Board):
    pass

class Square:

    list = []
    
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        Square.list.append(self)

    def print_list(self):
        for item in Square.list:
            print(item.value)

class Elements:
    def __init__(self, coords, type):
        self.coords = coords
        self.type = type

        if type == "element_row":
            print("Type is row")
        if type == "element_column":
            print("Type is column")
        if type == "element_box":
            print("Type is box")

    def legal_value(self):
        pass

        


if __name__ == "__main__":
    # Test code...
   
    reader = Sudoku_reader("sudoku_10.csv")
    board = Board(reader.next_board())
    print(board)
    print("NY KJØRING")
    

    #firkant = Square(1, 1, 10)
    squareboard = board._set_up_nums()
    
    ex_row = Elements(1, "element_row")
    ex_col = Elements(1, "element_column")
    ex_box = Elements(1, "element_box")
    #Square.print_list(list)
    

    #board._set_up_nums(board)

    #print(square)
    
    #board._set_up_nums(board)
    