# Secret Code Game

A fun and interactive game where players must guess a randomly generated secret code based on feedback clues. The game provides color-coded clues to help the player guess the secret code correctly.

## Features

- **Secret Code Generation**: A random secret code is generated with a user-defined number of digits (between 3 and 6).
- **Clue System**: After each guess, the game provides feedback using color-coded clues:
  - **Green**: The digit is in the secret code and in the correct position.
  - **Yellow**: The digit is in the secret code but in the wrong position.
  - **Red**: The digit is not in the secret code.
- **Dynamic Attempts**: The number of attempts varies based on the number of digits in the code (e.g., 8 attempts for a 3-digit code, 5 attempts for a 6-digit code).
- **Replay Option**: After finishing the game, players can choose to play again.

## How to Play

1. Choose the number of digits for the secret code (3 to 6 digits).
2. Guess the secret code based on the clues provided after each guess.
3. Use the color-coded clues to improve your next guess.
4. You have a limited number of attempts to crack the code.

## Example

If the secret code is `452` and the guess is `512`, the clue will be:

**Yellow** **Red** **Green**

This indicates that:
- **5** is in the secret code but in the wrong position (Yellow).
- **1** is not in the secret code (Red).
- **2** is in the secret code and in the correct position (Green).
