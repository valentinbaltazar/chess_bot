This is a project where I aim to build a chess bot from scratch, first in python then in C++

# Agent V0 vs Stockfish 1400 elo, depth=5

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

# Agent V1 vs Stockfish 1400 elo, depth=5

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

# Agent V2 vs Stockfish 1400 elo, depth=5

Current stats:
- Total Games 100
- Stockfish: 96
- Agent: 1
- Draws: 3

Eureaka!!! We won our first game against stock fish!

Agent update:
- Added evaluation strategy with pice-square tables (psqt)
- Uses piece value + psqt to determine the score
- Gredy algorithm, we do not search past the first available moves we sinply take the move with the best score

TO DO:
- Impelment search algorithm, evaluate at deeper levels for best move
- Can improve psqt or eval metric further