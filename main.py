import chess
import chess.engine
import random

def random_move(board):
  """Returns a random legal move for the current player."""
  legal_moves = list(board.legal_moves)
  return legal_moves[random.randint(0, len(legal_moves) - 1)]

# Path to the Stockfish executable
engine_path = "./engines/stockfish/stockfish-windows-x86-64-avx2.exe"


# Create a chess board
board = chess.Board()

# Start the Stockfish engine
with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
  move_count = 0
  while not board.is_game_over():
    # Get a random move from the bot
    bot_move = random_move(board) 
    board.push(bot_move) 
    move_count += 1

    # Get the best move from Stockfish
    result = engine.play(board, chess.engine.Limit(time=0.1)) 
    stockfish_move = result.move

    # Make Stockfish's move
    board.push(stockfish_move)
    move_count += 1

    print(f"Bot's move: {bot_move}")
    print(f"Stockfish's move: {stockfish_move}")
    print(board) 

print(board)
print(f"Number of moves: {move_count}")

# Determine the winner
result = board.result() 
if result == "1-0":
  print("Stockfish wins!")
elif result == "0-1":
  print("Random bot wins!")
elif result == "1/2-1/2":
  print("Draw!")
else:
  print("Unexpected result:", result) 