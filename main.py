from game import ChessMatch
from agent import ChessBot
from stock_fish import Stockfish


def main(n_games):
    engine_path = './engines/stockfish/stockfish-windows-x86-64-avx2.exe'

    chess_bot = ChessBot()
    stock_fish = Stockfish(engine_path)

    games = ChessMatch(chess_bot, stock_fish, n_games)

    res = games.play_all()

    # quit stockfish
    stock_fish.quit()

    return res

# Run some games
if __name__=='__main__':
    results = main(n_games=5)
    print(results)
