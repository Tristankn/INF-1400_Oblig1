from sudoku_reader import Sudoku_reader

# Klassen Board setter opp et spillebrett med lengde og bredde hentet fra en en 2D-liste returnert av Sudoku_reader
class Board:
   
    def __init__(self, nums):
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.rawnums = nums
        self.nums = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]

    # Printer ut et hvert spillebrett på en leselig måte
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        r += "[["
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + ", "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + "]"
        return r

# SudokuBoard er en subklasse av Board som er mer tilpasset et sudokubrett men benytter seg av samme oppsett for rad og kolonner.
class SudokuBoard(Board):
    
    def __init__(self, nums):
        super().__init__(nums)
        
    def _set_up_nums(self):
       # Leser inn tall fra self.rawnums og oppretter objekter av Square klassen hvor .value er verdien fra 2d-listen returnert fra sudoku_reader.
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                self.nums[i][j] = Square(self.rawnums[i][j])
        return self.nums

    def _set_up_elems(self):
        # Lager et nytt element for hver rad i self.nums
        for i in range(self.n_rows):
            element_row = Elements(self.nums[i])

        # Lager et nytt element for hver kolonne i self.nums
        for column in range(self.n_cols):
            element_column = Elements([self.nums[row][column] for row in range(self.n_cols)])
            for row in range(self.n_rows):
                self.nums[row][column].element_column = element_column

        # Lager et nytt element for hver 3x3 boks i self.nums. Metoden for å oppretter riktige boks-elementer er hentet fra chatgpt.
        for box_row in range(0, self.n_rows, 3):
            for box_col in range(0, self.n_cols, 3):
                box = [self.nums[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                element_box = Elements(box)
                for square in box:
                    square.element_box = element_box
                            
    def solve(self):
        # Løsningsalgoritme med backtracking. Baseres på å kjøre igjennom koden så fremst det finnes square objekter med .value == 0. 
        # Dersom is legal value tester alle tall 1-9 uten å finne en lovlig verdi vil koden backtracke til forrige square og prøve en annen lovlig verdi.
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

    # Denne funksjonen itererer igjennom 2d-listen og returnerer koordinatene til hver square som har .value == 0
    def find_empty_square(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if self.nums[i][j].value == 0:
                    return (i, j)
        return False
    # Printer ut sudokubrettet på en leselig måte
    def __str__(self):
        r = "Sudoku Board:\n"
        for row in self.nums:
            r += "["
            for square in row:
                r += str(str(square)) + " "
            r = r.strip() + "]\n"
        return r

    # Klassen Square representerer hver enkelt tallposisjon i sudokubrettet. 
    # Hvert objekt initeres med en verdi samt en tom referanse til hvilke elementer square objektet tilhører.
class Square:
    def __init__(self, value, element_row=None, element_column=None, element_box=None):
        
        self.value = value
        self.element_row = element_row
        self.element_column = element_column
        self.element_box = element_box 

    # Kjører metoden has_number for hver av elementene som er tilknyttet en gitt Square.
    # Alle if-sjekkene må være True for at funksjonen skal returne True
    def is_legal_value(self, number):
        if not self.element_row.has_number(number) and not self.element_column.has_number(number) and not self.element_box.has_number(number):
            return True

        else:
            return False

    # Definerer at når et Square objekt skal printes er det .value som skal printes ut slik at sudokubrettet blir mer leselig
    def __str__(self):
        return str(self.value)
    
# Klassen Elements representerer elementene rad, kolonne eller boks. Uavhengig av type element er hvert element kun en samling av ni square objekter.
class Elements:

    def __init__(self, element):
        self.element = element
        element_values = [sq.value for sq in self.element]

        # Setter referansene til square objektene slik at det er mulig å sjekke hvilken ni objekter den har i sin rad, kolonne og boks.
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
    
    # Returnerer True dersom et spesifikt tall allerede befinner seg i elementene en square er tilknytttet
    def has_number(self, number):
        element_values = [square.value for square in self.element]
        for square in self.element:
            if square.value == number:
                return True
        return False
       
if __name__ == "__main__":
    
    reader = Sudoku_reader("sudoku_10.csv")
    while SudokuBoard(reader.next_board()) is not None:
        blank_board = SudokuBoard(reader.next_board())
        blank_board._set_up_nums()
        blank_board._set_up_elems()
        blank_board.solve()
        print(blank_board) # Gjør programmet betydelig tregere men gir en fin visualisering av de løste sudokuene

    
     