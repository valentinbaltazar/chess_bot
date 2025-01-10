
import evaluate as Eval

def evaluate_position(board):
    """Evaluation metric to use when determining best move"""
    return Eval.Evaluation.evaluate(board)


def minimax(board, depth, max_player):
    """
    Minimax search algorithm.

    Args:
        board: The current game board state.
        depth: The maximum search depth.
        max_player: True if the current player is maximizing, False otherwise.

    Returns:
        A tuple containing:
            - The evaluation score of the current board state.
            - The best move for the current player.
    """

    if depth == 0 or board.is_game_over():
        return evaluate_position(board), None

    if max_player:
        best_move = None
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        best_move = None
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move