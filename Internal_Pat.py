
import sys # For cmd arguments
import random
from colorama import init, Fore
import matplotlib.pyplot as plt
from matplotlib.pyplot import text, ylabel, yticks
import numpy as np
import seaborn as sns

unvisited = "U"
open_space = "O"
wall = "H"
start = "S"
goal = "G"

def read_map(fn):
    grid = []
    with open(fn) as f:
        for line in f:
            grid.append(list(line.strip()))
    return np.asarray(grid)


def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == unvisited:
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == open_space:
                print(Fore.BLUE, f'{3}', end="")
            elif maze[i][j] == start:
                print(Fore.GREEN, f'{0}', end="")
            elif maze[i][j] == goal:
                print(Fore.GREEN, f'{1}', end="")
            else:
                print(Fore.RED, f'{2}', end="")
        print('') 

PAT = [0.0098863,0.0007578, 0.0049444, 0.0500344,0.1773686, 0.7564199,8.874657]
RL = [0.21, 0.521, 2.191, 8.511, 87.385, 280.6, 396.482]
sns.set()
XTicks = ['5x5', '10x10', '20x20', '40x40', '60x60', '100x100', '200x200']
plt.plot(PAT, label='PAT')
plt.plot(RL, label='RL')
plt.legend()
locs, labels = plt.xticks()
plt.xticks(locs[1:-1],XTicks)
plt.xlabel('Maze Sizes')
plt.ylabel('Run Time (s)')
plt.title('PAT Vs RL Execution Time')
plt.savefig('ExecutionTime')
plt.show()
