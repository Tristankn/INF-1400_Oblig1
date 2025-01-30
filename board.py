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
        # Setter opp rader med sine referanser til square objekter
        for i in range(self.n_rows):
            element_row = Elements(self.nums[i])

        # Setter opp kolonner med sine referanser til square objekter   
        for column in range(self.n_cols):
            element_column = Elements([self.nums[row][column] for row in range(self.n_cols)])
            for row in range(self.n_rows):
                self.nums[row][column].element_column = element_column

        # Setter opp bokser med sine referanser til square objekter HENTA FRA CHATGPT
        for box_row in range(0, self.n_rows, 3):
            for box_col in range(0, self.n_cols, 3):
                box = [self.nums[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                element_box = Elements(box)
                for square in box:
                    square.element_box = element_box

        
   
                            
                                
    def solve(self):
        solve_for_this_square = self.find_empty_square()
        if not solve_for_this_square:
            return True
        i, j = solve_for_this_square
        for number in range(1,10):
            if self.nums[i][j].is_legal_value(number):
                self.nums[i][j].value = number
                if self.solve():
                    return True
            self.nums[i][j].value = 0
        return False





    def find_empty_square(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.nums[i][j].value == 0:
                    return (i, j)
        return False
            
    def __str__(self):
        r = "Sudoku Board:\n"
        for row in self.nums:
            r += "["
            for square in row:
                r += str(str(square)) + " "
            r = r.strip() + "]\n"
        return r





        

class Square:
    
    def __init__(self, value, element_row=None, element_column=None, element_box=None):
        
        self.value = value
        self.element_row = element_row
        self.element_column = element_column
        self.element_box = element_box 
        #print(f"Created Square with( Value: {self.value}, Row: {self.element_row}, Column: {self.element_column}, Box: {self.element_box})")

    def is_legal_value(self, number):
        if not self.element_row.has_number(number) and not self.element_column.has_number(number) and not self.element_box.has_number(number):
            #print("Has returned true!")
            return True

        else:
            #print("Has returned false!")
            return False

    def __str__(self):
        return str(self.value)
    

class Elements:


    def __init__(self, element):
        self.element = element
        element_values = [sq.value for sq in self.element]
        #print(f"Initialized Elements with squares: {element_values}")

        for square in element:
            if square.element_row is None:
                square.element_row = self
            if square.element_column is None:
                square.element_column = self
            if square.element_box is None:
                square.element_box = self
        row_values = [sq.value for sq in element[0].element_row.element]
        col_values = [sq.value for sq in element[0].element_column.element]
        box_values = [sq.value for sq in element[0].element_box.element]
        #print(f"Initialized element with squares with( Value: {element[0].value}, Row: {row_values}, Column: {col_values}, Box: {box_values})")
        

    def has_number(self, number):
        element_values = [square.value for square in self.element]
        #print(f"Self.element verdier er: {element_values}")
        for square in self.element:
            if square.value == number:
                #print(f"square.value: {square.value}. Value: {number} found, returning True")
                return True
        #print(f"Value: {number} NOT found, returning False")
        return False
       

        


if __name__ == "__main__":
  
    reader = Sudoku_reader("sudoku_100.csv")
    for i in range (10):
        blank_board = SudokuBoard(reader.next_board())
        if blank_board is None:
            break
        blank_board._set_up_nums()
        blank_board._set_up_elems()
        blank_board.solve()
        print("Solved Sudokuboard: \n")
        print(blank_board)
    

    
     