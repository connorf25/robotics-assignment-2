
import sys # For cmd arguments
import random
from colorama import init, Fore
from matplotlib.pyplot import text
import numpy as np

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
maze = read_map("mazes/10_rl.txt")

print_maze(maze)