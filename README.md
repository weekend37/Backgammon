# Backgammon
Backgammon interface for the 2nd and 3rd projects in Computational Intelligence.

## The board interpretation
The game is set up in the **Backgammon.py** file. To play a game, simply run the program.
The two players are defined as player 1 and player -1.
The board has 29 positions:
- positions 1-24 are the labeled on-board positions
- positions 25 and 26 are the jails for when a piece is "killed" (25 is the jail for player 1 and 26 for player -1)
- positions 27 and 28 represent the position of the pieces who have been beard off (27 for player 1 and 28 for player -1)
- number 0 is pointless and is not being used...

The number of pieces in a certain possition of the board is represented by n where |n| is the number of pieces in the 
position and sign(n) indicates which player owns the pieces in the position. 

few examples:
- `board[23] = 3` means that player 1 has 3 player on the 23rd position of the board.
- `board[21] = -10` means that player -1 has 10 pieces on the 21st position of the board.
- `board[28] = -2` would mean that player -1 has beared off two pieces.

## Moves
The game is played between agents. Your main agent should be coded and trained in the **agent.py** file.
When the Backgammon.py program is executed, it imports your agent and uses his decisions to make moves.
The moves are simple. They are written as lists of two numbers where the 
- first number represents the position from where you wish to move your piece from 
- and the second number represents the position to where you wish to move your piece

When an agents is to move, it returns a couple of moves since he rolls two dices and therefore has to make two moves.
If there are less then 2 moves available (1 or 0) it can return fewer moves.

When a player rolls the same number on the dice in Backgammon, he is allowed to play 2 times. That is 2 moves 2 times.
When that happens, the agent should not return 4 moves in one. Instead, the **Backgammon.py** file asks the agent two times to make his move. 

To decide on which move to make feel free to use the functions *legal_moves*, *legal_move* and *update_board* as you wish as well as making your own versions of them.

example:
to make the following move: http://www.bkgm.com/faq/gif/pickandpass.gif
the agent of player 1 has to return the list ```[(10,5),(5,3)] ```

## Thoughts and advices
#### Running time
running time for one game is ~55ms per game or just under a minute per 1000 games (see time_test.py) when the players are only random agents that are not training. When training your agents, you might want to think cautiously about the time complexity of your code. Feel free to make your own faster code of Backgammon (and then share it!) but make sure your agents will be integrable for this version.
#### different perspectives
Your players have to be able to both play as player 1 and player -1. For this to be possible you can either 
  - flip the board and always make your player feel like player one. The code has already been made in the file **flipped_agent.py**.  There you can find the functions *flip_board* and *flip_move* as well as an example of an agent that uses them (hopefully) correctly.
  - account for both cases (as the moves will be different for the different players). Note that the training time will be twice as much as for the other option.
