#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 21:55:06 2018

@author: helgi
"""
import Backgammon
import time

start_time = time.time()
Backgammon.main()    
end_time = time.time()
total_time = end_time-start_time
print("total time: ", total_time)

