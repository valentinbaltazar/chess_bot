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
        move_list = []

        while not board.is_game_over():
            # Get move from white
            white_move = white_player.get_move(board)
            move_list.append(board.san(white_move))
            board.push(white_move)
    
            move_count += 1
            if board.is_game_over():
                break

            # Get move from black
            black_move = black_player.get_move(board)
            move_list.append(board.san(black_move))
            board.push(black_move)
        
            move_count += 1
            if board.is_game_over():
                break

            # print(f"White's move: {white_move}")
            # print(f"Black's move: {black_move}")
            # print(board)
    
        # print("*****Game Over*****")
        # print(board)
        # print(f"Number of moves: {move_count}")

        # Determine the winner
        result = board.result() 
        if result == "1-0":
            # print("White wins!")
            winner = "Agent" if self.is_white else "Stockfish"
        elif result == "0-1":
            # print("Black wins!")
            winner = "Stockfish" if self.is_white else "Agent"
        elif result == "1/2-1/2":
            # print("Draw!")
            winner = "Draw"
        else:
            print("Unexpected result:", result)
        
        # Reset the board for the next game, swap player colors
        board.reset()
        self.is_white = not self.is_white

        return (result, winner, move_list)
