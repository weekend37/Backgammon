# Backgammon
Backgammon interface for the final project in Computational Intelligence

## The board interpretation
The two players are defined as player 1 and player -1.
The board then currently has 29 positions:
- number 0 is not being used
- positions 1-24 are the labeled on-board positions
- positions 25 and 26 are the jails for when a piece is "killed" (25 is the jail for player 1 and 26 for player -1)
- positions 27 and 28 represent the position of the pieces who have been beard off (27 for player 1 and 28 for player -1)

The number of pieces in a certain possition of the board is represented by n where |n| is the number of pieces in the 
position and sign(n) indicates which player owns the pieces in the position. 

few examples:
- `board[23] = 3` means that player 1 has 3 player on the 23rd position of the board.
- `board[21] = -10` means that player -1 has 10 pieces on the 21st position of the board.
- `board[28] = -2` would mean that player -1 has beared off two pieces.


## Moves
info about the moves missing...

## Thoughts
- the 0 position is currently not used.. could possibly be used to indicate which player is to move to speed up the process
- running time for one game is ~0.06 seconds or just over a minute per 1000 games (see time_test.py)
- the developed agent should probably be coded as a seperate file
