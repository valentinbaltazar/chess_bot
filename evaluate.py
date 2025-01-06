from psqt import *

import chess

VALUE_MATE = 32000

# least significant bit
def lsb(x: int) -> int:
    return (x & -x).bit_length() - 1

def poplsb(x: int) -> int:
    x &= x - 1
    return x

def mate_in(ply: int) -> int:
    return VALUE_MATE - ply

def mated_in(ply: int) -> int:
    return ply - VALUE_MATE

class Evaluation:
    @staticmethod
    def eval_side(board: chess.Board, color: chess.Color) -> int:
        occupied = board.occupied_co[color]

        material = 0
        psqt = 0

        # loop over all set bits
        while occupied:
            # find the least significant bit
            square = lsb(occupied)

            piece = board.piece_type_at(square)

            # add material
            material += piece_values[piece]

            # add piece square table value
            psqt += (
                list(reversed(psqt_values[piece]))[square]
                if color == chess.BLACK
                else psqt_values[piece][square]
            )

            # remove lsb
            occupied = poplsb(occupied)

        return material + psqt

    @staticmethod
    def evaluate(board: chess.Board) -> int:
        return Evaluation.eval_side(board, chess.WHITE) - Evaluation.eval_side(
            board, chess.BLACK
        )