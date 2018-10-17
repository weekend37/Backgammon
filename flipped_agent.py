#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
an example of an intelligent agent who flips the board
"""
import numpy as np
import Backgammon

def flip_board(board_copy):
    #flips the game board and returns a new copy
    idx = np.array([0,24,23,22,21,20,19,18,17,16,15,14,13,
    12,11,10,9,8,7,6,5,4,3,2,1,26,25,28,27])
    flipped_board = -np.copy(board_copy[idx])
        
    return flipped_board

def flip_move(move):
    if len(move)!=0:
        for m in move:
            for m_i in range(2):
                m[m_i] = np.array([0,24,23,22,21,20,19,18,17,16,15,14,13,
                                12,11,10,9,8,7,6,5,4,3,2,1,26,25,28,27])[m[m_i]]        
    return move

def action(board_copy,dice,player,i):
    # the champion to be
    # inputs are the board, the dice and which player is to move
    # outputs the chosen move accordingly to its policy
    
    # starts by flipping the board so that the player always sees himself as player 1
    if player == -1: board_copy = flip_board(board_copy)
        
    # check out the legal moves available for the throw
    possible_moves, possible_boards = Backgammon.legal_moves(board_copy, dice, player=1)
    
    # if there are no moves available, return an empty move
    if len(possible_moves) == 0: 
        return [] 
    
    # Make the bestmove:
    # policy missing, returns a random move for the time being
    #
    #
    #
    #
    #
    move = possible_moves[np.random.randint(len(possible_moves))]
    
    # if the table was flipped the move has to be flipped as well
    if player == -1: move = flip_move(move)
    
    return move
