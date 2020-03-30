import numpy as np
import matplotlib.pyplot as plt

import Backgammon
import pubeval
import kotra
import randomAgent

def plot_perf(performance):
    plt.plot(performance)
    plt.show()
    return

def evaluate(agent, evaluation_agent, n_eval, n_games):
    wins = 0
    for i in range(n_eval):
        winner, board = Backgammon.play_a_game(agent, evaluation_agent)
        wins += int(winner==1)
    winrate = round(wins/n_eval*100,3)
    print("Win-rate after training for "+str(n_games)+" games: "+str(winrate)+"%" )
    return winrate

def train(n_games=200_000, n_epochs=5000, n_eval=1000):
    agent = kotra
    evaluation_agent = pubeval

    winrates = []
    for g in range(n_games):
        if g % n_epochs == 0 and g != 0:
            winrate = evaluate(agent, evaluation_agent, n_eval, n_games=g)
            winrates.append(winrate)

        winner, board = Backgammon.play_a_game(agent, agent, train=True, train_config={'g':g})
        agent.game_over_update(board, int(winner==1))
        agent.game_over_update(kotra.flip_board(board), int(winner==-1))
    
    plot_perf(winrates)

# ----- main -----
train()