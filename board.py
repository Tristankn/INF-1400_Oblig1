from sudoku_reader import Sudoku_reader

class Board:
   
    def __init__(self, nums):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.rawnums = nums
        self.nums = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]

        
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
    
    def __init__(self, nums):
        #self.sudoku_board = sudoku_board
        super().__init__(nums)
        
    def _set_up_nums(self):
        # Denne funksjonen må hente tall fra sudokureader og putte dem inn i stedet for None
        
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                self.nums[i][j] = Square(self.rawnums[i][j])
        return self.nums


    def _set_up_elems(self):
        #HENTA FRA CHATGPT, endre på?
        for i in self.nums:
            et_element_rad = Elements(i)
            
        for col_idx in range(self.n_cols):
            et_element_kolonne = Elements([self.nums[row_idx][col_idx] for row_idx in range(self.n_rows)])
        
        for box_row in range(0, self.n_rows, 3):
            for box_col in range(0, self.n_cols, 3):
                box = [self.nums[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                et_element_boks = Elements(box)

        
            
    def __str__(self):
        r = "Sudoku Board:\n"
        for row in self.nums:
            r += "["
            for square in row:
                r += str(str(square)) + " "
            r = r.strip() + "]\n"
        return r  





    def solve(self):
        
        pass

class Square:
    
    def __init__(self, value, row_element, col_element, box_element):
        
        self.value = value
        self.row_element = row_element
        self.col_element = col_element 
        self.box_element = box_element
    
    def __str__(self):
        return str(self.value)
    

class Elements:

    def __init__(self, row_element, col_element, box_element):
        self.row_element = row_element
        self.col_element = col_element
        self.box_element = box_element
        

        

    #ef legal_value(self, square, number):
    #   if number is in element:
    #       return False

    #def print_list_elements():
    #    for item in Elements.elements_list:
    #        print(item.squares)

        


if __name__ == "__main__":
    # Test code...
   
    #reader = Sudoku_reader("sudoku_10.csv")
    #board = Board(reader.next_board())
    ##print(board)
    #print("NY KJØRING")
    
# FAKTISK KJØRING AV KODE

    reader = Sudoku_reader("sudoku_10.csv")

    blank_board = SudokuBoard(reader.next_board())
    blank_board._set_up_nums()
    #print(sudokuboard)

    print(" ")
    print("STARTING TO SET UP ELEMENTS:")
    print(" ")
    blank_board._set_up_elems()
    print(" ")
    print("PRINTING OUT ELEMENTS")
    print(" ")
    print(blank_board)

    #print(squareboard)
    #print("Her")
    #print(blank_board)
    #print("Her")
    #Square.print_list(list)

    #blank_board._set_up_elems()
    #Elements.print_list_elements()

    #board._set_up_nums(board)

    #print(square)
    
    #board._set_up_nums(board)
    