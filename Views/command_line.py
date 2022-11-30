from Models.nested_array import ConnectN
from Models.cell_states import CellState

SYMBOLS = {
    CellState.EMPTY: " ",
    CellState.RED: "O",
    CellState.YELLOW: "X",
}

class Graphics:
    def __init__(self) -> None:
        pass

    def display_instructions(self):
        print("""
        Welcome to Connect-Four.

        There are a few rules before you get started...
        - Turns alternate.
        - You can only place tokens on the bottom row of a column.
        - First person to connect four tokens horizontally, vertically, or diagonally wins!
        """)

    def update_display(self, board: ConnectN):
        for row in range(board.rows - 1, -1, -1):
            print(f"{row + 1}: ", end="")
            for col in range(board.columns):
                symbol = SYMBOLS[board.get_position(row, col)]
                print(f"{symbol} ", end="")
            
            print()
        
        print("   ", end="")
        for col in range(board.columns):
            print(f"{col + 1} ", end="")
        print()

    def prompt_placement(self, current_turn: CellState):
        print(f"It is {SYMBOLS[current_turn]}'s turn. Submit the column you want to place a token.")
    
    def error_within_boundaries(self):
        print("Please place your token within the boundaries.")

    def get_column_to_place(self) -> int:
        return int(input())

    def congratulate_winner(self, winner: CellState):
        print(f"Yay, {SYMBOLS[winner]} is the winner!")
    
    def display_tie(self):
        print("Uh oh, it looks like you guys filled the board. This game must be declared a tie!")