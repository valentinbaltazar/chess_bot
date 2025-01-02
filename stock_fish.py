import chess
import chess.engine

class Stockfish:
    def __init__(self, engine_path, elo_rating=1400):
        """
        Initializes the Stockfish engine.

        Args:
            engine_path: Path to the Stockfish executable.
        """
       
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        self.engine.configure({"UCI_LimitStrength": True, "UCI_Elo": elo_rating})


    def get_move(self, board, search_depth=5):
        """
        Gets the best move from Stockfish for the given board position.

        Args:
            board: The current chess board.
            time_limit: Time limit for Stockfish to analyze the position in seconds.

        Returns:
            The best move as a chess.Move object.
        """
        result = self.engine.play(board, chess.engine.Limit(depth=search_depth))
        return result.move

    def quit(self):
        """
        Quits the Stockfish engine.
        """
        self.engine.quit()


if __name__ == "__main__":
    engine_path = "/path/to/stockfish"  
    stockfish = Stockfish(engine_path)

    board = chess.Board()

    # Get Stockfish's move
    stockfish_move = stockfish.get_move(board)
    print(f"Stockfish's move: {stockfish_move}")

    stockfish.quit()