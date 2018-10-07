#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:55:06 2018

@author: helgi
"""
import main
import time

# winner
winners = {}
winners["1"] = 0
winners["-1"] = 0

# games
games = []

# time
start_time = time.time()
N = 1000
for i in range(1000):
    w, g = main.play_a_game(commentary=False)
    winners[str(w)] += 1
    games.append(g)
    
end_time = time.time()
total_time = end_time-start_time

print("total time: ", total_time)
print("average time per game: ", total_time/N)    
print(winners)
print(games)

