#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Backgammon interface
Run this program to play a game of Backgammon
The agent is in another file
Most (if not all) of your agent-develeping code should be written in the agent.py file
However feel free to change this file as you wish.
"""
import numpy as np
import agent

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
    # rolls the dice
    dice = np.random.randint(1,7,2)
    return dice

def game_over(board):
    # returns True if the game is over
    return board[27]==15 or board[28]==-15

def check_for_error(board):
    # checks for obvious errors
    errorInProgram = False

    if (sum(board[board>0]) != 15 or sum(board[board<0]) != -15):
        # too many pieces on board
        errorInProgram = True
        print("To many pieces on board!")
    return errorInProgram

def pretty_print(board):
    string = str(np.array2string(board[1:13])+'\n'+
                 np.array2string(board[24:12:-1])+'\n'+
                 np.array2string(board[25:29]))
    print(string)

def flip_board(board):
    board = board * (-1)
    main_board = board[24:0:-1]
    jail1, jail2, off1, off2 = board[26], board[25], board[28], board[27]
    main_with_zero = np.insert(main_board, 0, board[0])
    new_board = np.append(main_with_zero, np.array([jail1, jail2, off1, off2]))
    return new_board



def legal_move(board, die):
    # finds legal moves for a board and one dice
    # inputs are some BG-board, the number on the die and which player is up
    # outputs all the moves (just for the one die)
    possible_moves = []

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
                # everybody's past the dice throw?
                s = np.max(np.where(board[1:7]>0)[0]+1)
                if s<die:
                    possible_moves.append(np.array([s,27]))

        possible_start_pips = np.where(board[0:25]>0)[0]

        # finding all other legal options
        for s in possible_start_pips:
            end_pip = s-die
            if end_pip > 0:
                if board[end_pip] > -2:
                    possible_moves.append(np.array([s,end_pip]))

    return possible_moves

def legal_moves(board, dice):
    # finds all possible moves and the possible board after-states
    # inputs are the BG-board, the dices rolled and which player is up
    # outputs the possible pair of moves (if they exists) and their after-states

    moves = []
    boards = []

    # try using the first dice, then the second dice
    possible_first_moves = legal_move(board, dice[0])
    for m1 in possible_first_moves:
        temp_board = update_board(board,m1)
        possible_second_moves = legal_move(temp_board,dice[1])
        for m2 in possible_second_moves:
            moves.append(np.array([m1,m2]))
            boards.append(update_board(temp_board,m2))

    if dice[0] != dice[1]:
        # try using the second dice, then the first one
        possible_first_moves = legal_move(board, dice[1])
        for m1 in possible_first_moves:
            temp_board = update_board(board,m1)
            possible_second_moves = legal_move(temp_board,dice[0])
            for m2 in possible_second_moves:
                moves.append(np.array([m1,m2]))
                boards.append(update_board(temp_board,m2))

    # if there's no pair of moves available, allow one move:
    if len(moves)==0:
        # first dice:
        possible_first_moves = legal_move(board, dice[0])
        for m in possible_first_moves:
            moves.append(np.array([m]))
            boards.append(update_board(temp_board,m))

        # second dice:
        possible_first_moves = legal_move(board, dice[1])
        for m in possible_first_moves:
            moves.append(np.array([m]))
            boards.append(update_board(temp_board,m))

    return moves, boards

def update_board(board, move):
    # updates the board
    # inputs are some board, one move and the player
    # outputs the updated board
    board_to_update = np.copy(board)

    # if the move is there
    if len(move) > 0:
        startPip = move[0]
        endPip = move[1]

        # moving the dead piece if the move kills a piece
        kill = board_to_update[endPip]==(-1)
        if kill:
            board_to_update[endPip] = 0
            jail = 26
            board_to_update[jail] = board_to_update[jail] - 1

        board_to_update[startPip] = board_to_update[startPip]-1
        board_to_update[endPip] = board_to_update[endPip]+1

    return board_to_update


def random_agent(board_copy,dice,i):
    # random agent
    # inputs are the board, the dice and which player is to move
    # outputs the chosen move randomly

    # check out the legal moves available for dice throw
    possible_moves, possible_boards = legal_moves(board_copy, dice)

    if len(possible_moves) == 0:
        return []
    else:
        move = possible_moves[np.random.randint(len(possible_moves))]
    return move

def play_a_game(commentary = True):
    board = init_board() # initialize the board
    player = 1 # player 1 starts

    # play on
    while not game_over(board): #and not check_for_error(board):
        if commentary: print("lets go player ",player)

        dice = roll_dice() # roll dice
        if commentary: print("rolled dices:", dice)

        # make a move (2 moves if the same number appears on the dice)
        for i in range(1+int(dice[0] == dice[1])):
            board_copy = np.copy(board)

            # make the move
            if player == 1:
                move = agent.action(board_copy,dice,1,i)
            elif player == -1:
                move = random_agent(board_copy,dice,i)

            # update the board
            if len(move) != 0:
                for m in move:
                    board = update_board(board, m)

            if commentary:
                print("move from player",player,":")
                print("board:")
                if(player == 1):
                    pretty_print(board)
                else:
                    pretty_print(flip_board(board))

        # players take turns
        player = -player
        board = flip_board(board)

    # return the winner
    return -1*player

def main():
    winners = {}; winners["1"]=0; winners["-1"]=0;
    nGames = 1
    for g in range(nGames):
        winner = play_a_game(commentary=True)
        winners[str(winner)] += 1
    print("out of", nGames, "games,")
    print("player", 1, "won", winners["1"],"times and")
    print("player", -1, "won", winners["-1"],"times")

if __name__ == '__main__':
    main()
