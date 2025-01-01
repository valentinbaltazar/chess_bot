"""
Start a game between a chess agent and stockfish/engine
"""
import chess
import chess.engine

class ChessMatch:

    def __init__(self, agent, engine, total_games):
        self.agent = agent
        self.engine = engine
        self.total_games = total_games
        self.outcomes = []
        # self.board = chess.Board()
        self.is_white = True # Agent will always play first as white

    def play_all(self):
        for i in range(self.total_games):
            outcome = self.play_match()
            self.outcomes.append((f"Game {i}", outcome))

        return self.outcomes


    def play_match(self):

        if self.is_white:
            white_player = self.agent
            black_player = self.engine
        else:
            white_player = self.engine
            black_player = self.agent

        board = chess.Board()
        move_count = 0

        while not board.is_game_over():
            # Get move from white
            white_move = white_player.get_move(board)
            board.push(white_move)
            move_count += 1
            if board.is_game_over():
                break

            # Get move from black
            black_move = black_player.get_move(board)
            board.push(black_move)
            move_count += 1
            if board.is_game_over():
                break

            print(f"White's move: {white_move}")
            print(f"Black's move: {black_move}")
            print(board)
    
        print("*****Game Over*****")
        print(board)
        print(f"Number of moves: {move_count}")

        # Determine the winner
        result = board.result() 
        if result == "1-0":
            print("White wins!")
        elif result == "0-1":
            print("Black wins!")
        elif result == "1/2-1/2":
            print("Draw!")
        else:
            print("Unexpected result:", result)
        
        # Reset the board for the next game, swap player colors
        board.reset()
        self.is_white = not self.is_white

        return result
