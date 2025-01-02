This is a project where I aim to build a chess bot from scratch, first in python then in C++

# V0 Stockfish 1400 elo, depth=5

Fixed Stockfish elo at 1400 and depth=5, once we beat this I will increase the difficulty.

Current stats:
- Total Games 100
- Stockfish: 100
- Agent: 0
- Draws: 0

Basic building blocks working including:
- Chess match between a custom agent and Stockfish chess engine
- Plays N many games and logs the matches and scores
- Can print to terminal

TO DO:
- Current agent is a "random" bot which plays a random chess move, need to inplement a better evaluation strategy
- Would be nice to have a UI for chess macthes

# V1 Stockfish 1400 elo, depth=5

Current stats:
- Total Games 100
- Stockfish: 94
- Agent: 0
- Draws: 6

Success!!

Agent update:
- random agent was onbviously poor
- new agent uses priority of moves checkmate, captures, promotions

It does not win but draws in some cases, which is not bad for such a simple chess bot.

