from game import ChessMatch
from agent import ChessBot
from stock_fish import Stockfish

name1 = "greedy"
name2 = "minimax"


def main(n_games):
    engine_path = './engines/stockfish/stockfish-windows-x86-64-avx2.exe'

    chess_bot1 = ChessBot(name=name1)
    chess_bot2 = ChessBot(name=name2)
    # chess_bot2 = Stockfish(engine_path)

    games = ChessMatch(chess_bot1, chess_bot2, n_games)

    res = games.play_all()

    # quit stockfish
    # stock_fish.quit()

    return res

# post processing

def win_loss(results):
    chess_bot1 = sum([1 for n in results if n[1][1]==name1])
    chess_bot2 = sum([1 for n in results if n[1][1]==name2])
    draws = sum([1 for n in results if n[1][1]=="Draw"])

    print(f"Total Games {len(results)}")
    print(f"{name1}: {chess_bot1}")
    print(f"{name2}: {chess_bot2}")
    print(f"Draws: {draws}")

    

# Run some games
if __name__=='__main__':
    results = main(n_games=40)
    # print(results)
    win_loss(results)

