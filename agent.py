"""
Create an agent class which returns a move
"""
import chess
import random

class ChessBot:
    """Returns a legal move for the given board state"""

    # def __init__(self, board):
    #     self.board = board
    
    def get_move(self, board):
        legal_moves = list(board.legal_moves)
        print(legal_moves)
        return legal_moves[random.randint(0, len(legal_moves)-1)]
    
    def evaluate_position(self):
        """Evaluation metric to use when determining best move"""
        return None

    
