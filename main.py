#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backgammon interface

@author: helgi
"""
import numpy as np

def init_board():
    # initializes the game board
   
    board = np.zeros(29)
    board[1] = -2
    board[12] = -5
    board[17] = -3
    board[19] = -5
    board[6] = 5
    board[8] = 3
    board[13] = 5
    board[24] = 2
    return board

def roll_dice():
    # rolls the dices
    dice = np.random.randint(1,7,2)
    return dice

def game_over(board):
    # returns True if the game is over    
    return board[27]==15 or board[28]==-15

def check_for_error(board):
    # checks for obvious errors
    # should probably not be in the final version
    errorInProgram = False
    
    if (sum(board[board>0]) != 15 or sum(board[board<0]) != -15):
        # too many pieces on board
        errorInProgram = True
        print("To many pieces on board!")
    return errorInProgram
    
    
def legal_move(board, die, player):
    # finds legal moves for a board and one dice
    # inputs are some BG-board, the number on the die and which player is up
    # outputs all the moves (just for the one die)
    possible_moves = []

    if player == 1:
        
        # dead piece, needs to be brought back to life
        if board[25] > 0: 
            start_pip = 25-die
            if board[start_pip] > -2:
                possible_moves.append(np.array([25,start_pip]))
                
        # no dead pieces        
        else:
            # adding options if player is bearing off
            if sum(board[7:25]>0) == 0: 
                if (board[die] > 0):
                    possible_moves.append(np.array([die,27]))
                    
                elif not game_over(board): # smá fix
                    if np.max(np.where(board[1:7]>0)[0]+1)<die:
                        # everybody's past the dice throw
                        possible_start_pips = np.where(board[1:7]>0)[0]+1
                        for s in possible_start_pips:
                            possible_moves.append(np.array([s,27]))
                    
            possible_start_pips = np.where(board[0:25]>0)[0]

            # finding all other legal options
            for s in possible_start_pips:
                end_pip = s-die
                if end_pip > 0:
                    if board[end_pip] > -2:
                        possible_moves.append(np.array([s,end_pip]))
                        
    elif player == -1:
        # dead piece, needs to be brought back to life
        if board[26] < 0: 
            start_pip = die
            if board[start_pip] < 2:
                possible_moves.append(np.array([26,start_pip]))
                
        # no dead pieces       
        else:
            # adding options if player is bearing off
            if sum(board[1:19]<0) == 0: 
                if (board[25-die] < 0):
                    possible_moves.append(np.array([25-die,28]))
                elif not game_over(board): # smá fix
                    if np.max(np.where(board[19:25][::-1]<0)[0]+1)<die:
                        # everybody's past the dice throw
                        possible_start_pips = np.where(board[19:25]<0)[0]+19
                        for s in possible_start_pips:
                            possible_moves.append(np.array([s,28]))

            # finding all other legal options
            possible_start_pips = np.where(board[0:25]<0)[0]
            for s in possible_start_pips:
                end_pip = s+die
                if end_pip < 25:
                    if board[end_pip] < 2:
                        possible_moves.append(np.array([s,end_pip]))
        
    return possible_moves

def legal_moves(board, dice, player):
    # finds all possible moves and the possible board after-states
    # inputs are the BG-board, the dices rolled and which player is up
    # outputs the possible pair of moves (if they exists) and their after-states

    moves = []
    boards = []

    # try using the first dice, then the second dice
    possible_first_moves = legal_move(board, dice[0], player)
    for m1 in possible_first_moves:
        temp_board = update_board(board,m1,player)
        possible_second_moves = legal_move(temp_board,dice[1], player)
        for m2 in possible_second_moves:
            moves.append(np.array([m1,m2]))
            boards.append(update_board(temp_board,m2,player))
        
    # try using the second dice, then the first one
    possible_first_moves = legal_move(board, dice[1], player)
    for m1 in possible_first_moves:
        temp_board = update_board(board,m1,player)
        possible_second_moves = legal_move(temp_board,dice[0], player)
        for m2 in possible_second_moves:
            moves.append(np.array([m1,m2]))
            boards.append(update_board(temp_board,m2,player))
            
    # if there's no pair of moves available, allow one move:
    if len(moves)==0: 
        # first dice:
        possible_first_moves = legal_move(board, dice[0], player)
        for m in possible_first_moves:
            moves.append(np.array([m]))
            boards.append(update_board(temp_board,m,player))
            
        # second dice:
        possible_first_moves = legal_move(board, dice[1], player)
        for m in possible_first_moves:
            moves.append(np.array([m]))
            boards.append(update_board(temp_board,m,player))
            
    return moves, boards 

def update_board(board, move, player):
    # updates the board
    # inputs are some board, one move and the player
    # outputs the updated board
    
    # copying the board is needed for some reason
    board_to_update = np.copy(board) 

    # if the move is there
    if len(move) > 0:
        startPip = move[0]
        endPip = move[1]
        
        # moving the dead piece if the move kills a piece
        kill = board_to_update[endPip]==(-1*player)
        if kill:
            board_to_update[endPip] = 0
            jail = 25+(player==1)
            board_to_update[jail] = board_to_update[jail] - player
        
        board_to_update[startPip] = board_to_update[startPip]-1*player
        board_to_update[endPip] = board_to_update[endPip]+player

    return board_to_update
    
    
def random_agent(boards,moves):
    # player -1
    # agent with random policy 
    # takes in all the possible moves and chooses a random one
    if len(moves) == 0:
        # if there aren't any possible moves
        return []
    else: 
        move = moves[np.random.randint(len(moves))]
    return move
    
def agent(boards,moves):
    # the champion to be 
    # should, in my opinion, be in another file
    # inputs are the possible boards and the possible moves
    # outputs the chosen move accordingly to its policy
    
    if len(moves) == 0:
        # if there aren't any possible moves
        return []
    else: 
        # missing policy, returns a random move for the time being
        move = moves[np.random.randint(len(moves))]
    return move

# __main__
board = init_board() # initialize the board
player = 1 # player 1 starts
numberOfTurns = 0
printCommands = True

# play on
while (not game_over(board) and not check_for_error(board)):
    if printCommands: print("lets go player ",player)
    
    dice = roll_dice() # roll dice
    if printCommands: print("rolled dices:", dice)
    
    # make a move (2 moves if the same number appears on the dices)
    for i in range(1+int(dice[0] == dice[1])):
        # check out the legal moves available for dice
        board_copy = np.copy(board) # skrýtið að þetta þurfti
        possible_moves, possible_boards = legal_moves(board_copy, dice, player)
        # if printCommands: print("possible moves: ", possible_moves)
        
        # use your policy to pick the best move
        if player == 1:
            move = agent(possible_boards, possible_moves)
        elif player == -1:
            move = random_agent(possible_boards, possible_moves)
            
        # need to make sure the move is one of the possible moves
        # maybe only use integers as an output of the agents?
        if printCommands: print("move chosen by player ",player,":",move)
        
        # make the move and update the board
        for m in move:
            board = update_board(board, m, player)
    
        if printCommands: print("the board after his move: ", board)

    # players take turns 
    player = -player
    
    # count the turns
    numberOfTurns += 1
    print("number of rounds:", int(np.floor(numberOfTurns/2)), "\n \n \n")
