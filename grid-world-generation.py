import random
from colorama import init, Fore
# colorama needs to be initialized in order to be used
init()
def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'O':
                print(Fore.BLUE, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'S':
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            elif maze[i][j] == 'G':
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('') 

def initialize_maze(w, h):
    maze = []
    for i in range(0, h):
        line = []
        for j in range(0, w):
            line.append('u')
        maze.append(line)
    return maze

def not_edge(x, edge):
    if x == 0:
        x += 1
    if x == edge - 1:
        x -= 1
    return x

open = "O"
wall = "H"
start = "S"
goal = "G"

def generate_maze (width, height):
    walls = []
    # Initialize maze
    maze = initialize_maze(width, height)
    # Random starting coordinates which are not on edge of world
    starting_x = int(random.random() * width)
    starting_x = not_edge(starting_x, width)
    starting_y = int(random.random() * height)
    starting_y = not_edge(starting_y, height)
    # Mark starting point
    maze[starting_y][starting_x] = start
    walls.append([starting_y-1, starting_x])
    walls.append([starting_y, starting_x-1])
    walls.append([starting_y, starting_x+1])
    walls.append([starting_y+1, starting_x])
    print_maze(maze)

generate_maze(10, 10)


