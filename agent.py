"""
Create an agent class which returns a move
"""
import chess
import random

import evaluate as Eval
from search import minimax

class ChessBot:
    """Returns a legal move for the given board state"""

    def __init__(self, name):
        self.name = name # will call different methods
    
    def get_move(self, board, is_max):
        """Each method is a different bot, specified by name"""
        if self.name == "random":
            return self.random_bot(board)
        elif self.name == "priority":
            return self.checkmate_priority(board)
        elif self.name == "greedy":
            # use evaluation to pick best move (no depth searching)
            return self.greedy_max(board)
        elif self.name == "minimax":
            return self.minimax_bot(board, 2, is_max) # depth of 2 for testing
        else:
            return None

    def minimax_bot(self, board, depth, is_max):
        """Evaluates positions and returns best move at specified depth"""
        eval, move = minimax(board, depth, is_max)
        return move
    
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
    
    def random_bot(self, board):
        legal_moves = list(board.legal_moves)
        return random.choice(legal_moves)
