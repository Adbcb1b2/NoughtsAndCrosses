# NoughtsAndCrosses
An unbeatable noughts and crosses game, written in python

# Noughts and Crosses Game

This project is a simple implementation of the classic **Noughts and Crosses (Tic-Tac-Toe)** game. Players can enjoy the game against the computer in the Python console, as well as manage their scores using a leaderboard stored in a JSON-formatted text file. 

---

## Features
- **Interactive Gameplay**: Play noughts and crosses against the computer.
- **AI Opponent**: The computer selects strategic moves to challenge the player.
- **Leaderboard Management**:
  - Save your score to the leaderboard.
  - Load and display scores from a leaderboard stored in `leaderboard.txt`.
- **Modular Design**: The script can be imported as a module for further use and enhancements.

---

## File Requirements
- A text file named `leaderboard.txt` is required for saving and loading scores.
- **Important**: The text file must contain JSON-formatted data with key-value pairs in the format:
  ```json
  {
      "Name": Score
  }
  
  {
      "Alice": 5,
      "Bob": 2,
      "Charlie": 8
  }
