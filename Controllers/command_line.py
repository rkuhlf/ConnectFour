
from Models.nested_array import ConnectN
from Views.command_line import Graphics
from Models.cell_states import CellState

class Controller:
    def __init__(self) -> None:
        self.board = ConnectN()
        self.graphics = Graphics()

        self.winner = None
        self.current_turn = CellState.YELLOW
    
    def swap_turn(self):
        if self.current_turn == CellState.YELLOW:
            self.current_turn = CellState.RED
        else:
            self.current_turn = CellState.YELLOW

    # TODO: move more of this logic to the view.
    # Controller should really only be a state engine.
    def play(self):
        """
        Method to play the game. Only one that must be called by outside function to play game.
        """

        self.graphics.display_instructions()

        while True:
            while not self.board.is_board_full():
                self.graphics.update_display(self.board)

                self.graphics.prompt_placement(self.current_turn)

                
                column = self.graphics.get_column_to_place() - 1
                
                try:
                    is_winning = self.board.place_piece(column, self.current_turn)
                except ValueError:
                    self.graphics.error_within_boundaries()
                    continue

                if is_winning:
                    self.winner = self.current_turn
                    self.graphics.update_display(self.board)

                    break

                self.swap_turn()

            # If we break out of the loop, the game is over
            if self.winner is not None:
                self.graphics.congratulate_winner(self.winner)
            else:
                self.graphics.display_tie()



            self.board.clear()

        

        

        