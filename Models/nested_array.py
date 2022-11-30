
from Models.cell_states import CellState

REPR_SYMBOLS = {
    CellState.EMPTY: "O",
    CellState.YELLOW: "Y",
    CellState.RED: "R"
}

def get_repr_symbol(val: CellState):
    return REPR_SYMBOLS[val]

def generate_board(rows, columns):
    """
    Generates a 2D matrix of cell states
    """

    return [ [CellState.EMPTY]*columns for i in range(rows)]
    
class ConnectN:
    def __init__(self, rows=6, columns=7, to_connect=4) -> None:
        self.rows = rows
        self.columns = columns
        self.to_connect = to_connect
        # The bottom of the board is the zero-th row
        self.board = generate_board(rows, columns)

    def get_position(self, row: int, col: int):
        self.check_valid(row, col)
        
        return self.board[row][col]
    
    def set_position(self, row: int, col: int, val: CellState):
        self.board[row][col] = val

    def place_piece(self, column: int, piece_type: CellState):
        if self.is_column_full(column):
            raise ValueError("No more pieces can be placed in that column.")
        
        row = 0
        while (self.get_position(row, column) != CellState.EMPTY):
            row += 1

        self.set_position(row, column, piece_type)
        
        if self.is_piece_winning(row, column):
            return True
        
        return False
    

    def count_in_direction(self, row: int, col: int, row_direction: int, col_direction):
        if self.get_position(row, col) == CellState.EMPTY:
            raise ValueError("There is no piece placed at the indicated row and column.")
        
        target_type = self.get_position(row, col)

        pieces = 1
        while (self.is_valid_position(row + row_direction, col + col_direction)
               and self.board[row + row_direction][col + col_direction] == target_type):
            pieces += 1
            row, col = row + row_direction, col + col_direction
        
        return pieces

    def count_in_both_directions(self, row: int, col: int, row_direction: int, col_direction):
        self.check_valid(row, col)

        count = self.count_in_direction(row, col, row_direction, col_direction)
        count += self.count_in_direction(row, col, -row_direction, -col_direction)

        return count - 1

    def is_piece_winning(self, row: int, column: int):
        """
        Returns whether a specific piece is a part of a connect-n
        """
        self.check_valid(row, column)

        # Horizontal count
        if self.count_in_both_directions(row, column, 0, 1) >= self.to_connect:
            return True
        
        # Vertical count
        if self.count_in_both_directions(row, column, 1, 0) >= self.to_connect:
            return True
        
        # Diagonal up-right count
        if self.count_in_both_directions(row, column, 1, 1) >= self.to_connect:
            return True
        
        # Diagonal up-left count
        if self.count_in_both_directions(row, column, 1, -1) >= self.to_connect:
            return True
        
        return False


    def check_valid(self, row: int, col: int):
        if not self.is_valid_position(row, col):
            raise ValueError(f"The given position, ({row}, {col}), must be within the board.")

    def is_valid_position(self, row: int, col: int):
        if row < 0:
            return False
        
        if col < 0:
            return False
        
        if row >= self.rows:
            return False
        
        if col >= self.columns:
            return False
        
        return True

    def is_column_full(self, column):
        for row in range(self.rows):
            if self.get_position(row, column) == CellState.EMPTY:
                return False
        
        return True

    def is_board_full(self):
        for column in range(self.columns):
            if not self.is_column_full(column):
                return False
        
        return True


    def clear(self) -> None:
        self.board = generate_board(self.rows, self.columns)


    def __repr__(self) -> str:
        ans = ""
        for row in self.board:
            row = map(get_repr_symbol, row)
            ans += ", ".join(row)
            ans += "\n"

        return ans


if __name__ == "__main__":
    board = ConnectN()

    print(board.board)