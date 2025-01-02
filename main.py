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

# post processing

def win_loss(results):
    engine_wins = sum([1 for n in results if n[1][1]=="Stockfish"])
    agent_wins = sum([1 for n in results if n[1][1]=="Agent"])
    draws = sum([1 for n in results if n[1][1]=="Draw"])

    print(f"Total Games {len(results)}")
    print(f"Stockfish: {engine_wins}")
    print(f"Agent: {agent_wins}")
    print(f"Draws: {draws}")

    

# Run some games
if __name__=='__main__':
    results = main(n_games=100)
    # print(results)
    win_loss(results)

