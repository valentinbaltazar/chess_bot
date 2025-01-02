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
        # print(legal_moves)
        # return random.randint(0, len(legal_moves)-1)
        return self.checkmate_priority(board)
    
        
    def evaluate_position(self):
        """Evaluation metric to use when determining best move"""
        return None

        
        
    def checkmate_priority(self, board):
    
        moves = list(board.legal_moves)

        # 1. Check for checkmate
        for move in moves:
            board_copy = board.copy()
            board_copy.push(move)
            if board_copy.is_checkmate():
                return move

        # 2. Check for captures
        for move in moves:
            if board.piece_at(move.to_square) is not None:
                return move

        # 3. Check for queen promotions
        for move in moves:
            if move.promotion is not None:
                return move

        # 4. Return a random move
        return random.choice(moves)