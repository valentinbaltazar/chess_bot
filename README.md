# Chess Bot Development Project 🎮

This repository hosts my journey of building a chess bot from scratch. The project starts in Python, with plans to later transition to C++ for improved performance. The ultimate goal is to create a competitive chess-playing agent capable of challenging higher-rated opponents over time.

---

## Project Overview 🔄

### Agent vs Stockfish Matches 🌀

#### **Agent V0 vs Stockfish 1400 Elo (Depth = 5)**
- Fixed Stockfish Elo: 1400
- Fixed Stockfish Search Depth: 5
- Objective: Beat Stockfish at this level before increasing the difficulty.

**✨ Current Stats:**
- Total Games: 100
- Stockfish Wins: 100
- Agent Wins: 0
- Draws: 0

**🔧 Implemented Features:**
- Chess matches between a custom agent and the Stockfish chess engine.
- Automated gameplay over multiple matches, with logging of results.
- Match results can be printed to the terminal.

**🔎 To-Do List:**
1. Replace the current random-move bot with an evaluation strategy.
2. Develop a user interface (UI) for interactive chess matches.

---

#### **Agent V1 vs Stockfish 1400 Elo (Depth = 5)**
**✨ Current Stats:**
- Total Games: 100
- Stockfish Wins: 94
- Agent Wins: 0
- Draws: 6

**🎉 Success Achieved!**
- The first non-losing results: 6 draws against Stockfish.

**🔄 Agent Updates:**
- Replaced random move selection with a priority-based approach:
  - Prioritizes moves like check, capture, and promotion.
- Although the bot doesn’t win, achieving draws is a significant milestone for such a simple agent.

---

#### **Agent V2 vs Stockfish 1400 Elo (Depth = 5)**
**✨ Current Stats:**
- Total Games: 100
- Stockfish Wins: 96
- Agent Wins: 1
- Draws: 3

**🌟 Major Breakthrough!**
- The bot achieved its first victory against Stockfish.

**🔄 Agent Updates:**
- Introduced a Greedy Algorithm using piece-square tables (PSQT):
  - Evaluates moves based on piece value and position on the board.
  - Chooses the move with the highest evaluation score.
- The bot currently evaluates only one ply (single move ahead).

**🔎 To-Do List:**
1. Implement a search algorithm for deeper move evaluation.
2. Optimize the evaluation metric and piece-square tables.

---

### Agent vs Agent Matches 🎮🕵️

To evaluate performance, different versions of the bot are pitted against each other:
- **Random Bot**: Makes a random legal move.
- **Priority Bot**: Chooses the first move that is a check, capture, or promotion.
- **Greedy Bot**: Selects the move with the highest evaluation score using PSQT.

#### **Random Bot vs Priority Bot**
**⚔️ Outcome:**
- Total Games: 100
- Random Bot Wins: 0
- Priority Bot Wins: 91
- Draws: 9

**🕵️ Insights:**
- The Random Bot never wins and rarely draws.
- The Priority Bot dominates due to its simplistic yet effective strategy.

---

#### **Priority Bot vs Greedy Bot**
**⚔️ Outcome:**
- Total Games: 100
- Greedy Bot Wins: 4
- Priority Bot Wins: 18
- Draws: 78

**🕵️ Insights:**
- The Priority Bot outperforms the Greedy Bot, likely due to the Greedy Bot’s inability to evaluate deeper positions.
- Adding search capabilities to the Greedy Bot could significantly improve its performance.

---

#### **Greedy Bot vs Random Bot**
**⚔️ Outcome:**
- Total Games: 100
- Greedy Bot Wins: 18
- Random Bot Wins: 0
- Draws: 82

**🕵️ Insights:**
- Surprisingly, the Greedy Bot struggles to dominate the Random Bot, drawing most of the games.
- This highlights the need for further improvements in the Greedy Bot’s strategy.

---

## Next Steps 🚀

1. **Algorithm Improvements:**
   - Implement Alpha-Beta pruning for efficient search.
   - Introduce iterative deepening for better move evaluation.
2. **UI Development:**
   - Create a user-friendly interface for human vs. bot matches.
   - Visualize match results and agent performance metrics.
3. **Transition to C++:**
   - Rewrite the project in C++ for faster execution and scalability.
4. **Advanced Features:**
   - Develop reinforcement learning agents.
   - Incorporate neural networks for advanced evaluation metrics.

---

## Conclusion 🏆
This project showcases the iterative development of a chess bot, starting with simple strategies and progressively building toward more advanced capabilities. Each milestone represents a step forward in understanding and implementing key principles of chess AI.

Stay tuned for future updates as the bot evolves! 🎮🚀

