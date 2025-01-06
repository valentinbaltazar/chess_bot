"""
Create an agent class which returns a move
"""
import chess
import random

import evaluate as Eval

class ChessBot:
    """Returns a legal move for the given board state"""

    # def __init__(self, board):
    #     self.board = board
    
    def get_move(self, board):
        # legal_moves = list(board.legal_moves)
        # print(legal_moves)
        # return random.randint(0, len(legal_moves)-1)
        # return self.checkmate_priority(board)

        # use evaluation to pick best move (no depth searching)
        return self.greedy_max(board)

    def greedy_max(self, board):
        # use eval and take best move without move search
        legal_moves = list(board.legal_moves)
        move_values = []
        
        white_turn =  board.turn

        for move in legal_moves:
            board_copy = board.copy()
            board_copy.push(move)

            # get score for each move
            score = self.evaluate_position(board_copy)
            move_values.append((move, score))
        

        best_move, best_score = max(move_values, key=lambda x: x[1]) if white_turn else min(move_values, key=lambda x: x[1])
        
        return best_move





            

    def evaluate_position(self, board):
        """Evaluation metric to use when determining best move"""
        return Eval.Evaluation.evaluate(board)

        
        
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
    
    