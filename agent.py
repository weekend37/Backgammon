#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
the agent
"""
import numpy as np
import Backgammon

def action(board_copy,dice,player,i):
    # the champion to be
    # inputs are the board, the dice and which player is to move
    # outputs the chosen move accordingly to its policy
    move = []
    
    # check out the legal moves available for the throw
    possible_moves, possible_boards = Backgammon.legal_moves(board_copy, dice, player)
    
    # make the best move according to the policy
    if len(possible_moves) != 0:
        move = policy(possible_moves,possible_boards,dice,i)

    return move
    

def policy(possible_moves, possible_boards, dice, i):
    # missing policy, returns a random move for the time being
    #
    #
    #
    #
    #
    move = possible_moves[np.random.randint(len(possible_moves))]
    return move