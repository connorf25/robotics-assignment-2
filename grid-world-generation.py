import sys # For cmd arguments
import random
from colorama import init, Fore
from matplotlib.pyplot import text
# colorama needs to be initialized in order to be used
init()

unvisited = "U"
open_space = "O"
wall = "H"
start = "S"
goal = "G"

def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == unvisited:
                print(Fore.WHITE, f'{maze[i][j]}', end="")
            elif maze[i][j] == open_space:
                print(Fore.BLUE, f'{maze[i][j]}', end="")
            elif maze[i][j] == start:
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            elif maze[i][j] == goal:
                print(Fore.GREEN, f'{maze[i][j]}', end="")
            else:
                print(Fore.RED, f'{maze[i][j]}', end="")
        print('') 

def initialize_maze(w, h):
    maze = []
    for i in range(0, h):
        line = []
        for j in range(0, w):
            line.append(unvisited)
        maze.append(line)
    return maze

def not_edge(x, edge):
    if x == 0:
        x += 1
    if x == edge - 1:
        x -= 1
    return x

def surrounding_cells(rand_wall, maze):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == open_space):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == open_space):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == open_space):
        s_cells +=1
    if (maze[rand_wall[0]][rand_wall[1]+1] == open_space):
        s_cells += 1
    return s_cells

def find_wall(rand_wall, walls):
    for i in range(len(walls)):
        if (walls[i][0] == rand_wall[0] and walls[i][1] == rand_wall[1]):
            return i

def handle_neighbor(direction, width, height, random_wall, maze, walls):
    if direction == "up":
        if (random_wall[0] != 0):
            if (maze[random_wall[0]-1][random_wall[1]] != open_space):
                maze[random_wall[0]-1][random_wall[1]] = wall
            if ([random_wall[0]-1, random_wall[1]] not in walls):
                walls.append([random_wall[0]-1, random_wall[1]])
        return maze, walls

    if direction == "down":
        if (random_wall[0] != height - 1):
            if (maze[random_wall[0]+1][random_wall[1]] != open_space):
                maze[random_wall[0]+1][random_wall[1]] = wall
            if ([random_wall[0]+1, random_wall[1]] not in walls):
                walls.append([random_wall[0]+1, random_wall[1]])
        return maze, walls
        
    if direction == "left":
        if (random_wall[1] != 0):
            if (maze[random_wall[0]][random_wall[1]-1] != open_space):
                maze[random_wall[0]][random_wall[1]-1] = wall
            if ([random_wall[0], random_wall[1]-1] not in walls):
                walls.append([random_wall[0], random_wall[1]-1])
        return maze, walls

    if direction == "right":
        if (random_wall[1] != width - 1):
            if (maze[random_wall[0]][random_wall[1]+1] != open_space):
                maze[random_wall[0]][random_wall[1]+1] = wall
            if ([random_wall[0], random_wall[1]+1] not in walls):
                walls.append([random_wall[0], random_wall[1]+1])
        return maze, walls


def generate_maze (width, height):
    walls = []
    # Initialize maze
    maze = initialize_maze(width, height)
    # Random starting coordinates which are not on edge of world
    starting_x = int(random.random() * width)
    starting_x = not_edge(starting_x, width)
    starting_y = int(random.random() * height)
    starting_y = not_edge(starting_y, height)
    # Mark starting point as open_space
    maze[starting_y][starting_x] = open_space
    walls.append([starting_y-1, starting_x])
    walls.append([starting_y, starting_x-1])
    walls.append([starting_y, starting_x+1])
    walls.append([starting_y+1, starting_x])
    maze[starting_y-1][starting_x] = wall
    maze[starting_y][starting_x-1] = wall
    maze[starting_y][starting_x+1] = wall
    maze[starting_y+1][starting_x] = wall
    while walls:
        # Pick a random wall
        random_wall = walls[int(random.random()*len(walls))-1]

        # Check if the wall is a left wall
        if random_wall[1] != 0 and maze[random_wall[0]][random_wall[1]-1] == unvisited and maze[random_wall[0]][random_wall[1]+1] == open_space:
            s_cells = surrounding_cells(random_wall, maze)
            if s_cells < 2:
                # Mark cell as open_space
                maze[random_wall[0]][random_wall[1]] = open_space
                # Handle neighbor operations
                maze, walls = handle_neighbor("up", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("down", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("left", width, height, random_wall, maze, walls)
            walls.remove(random_wall)
            continue
                    
        # Check if wall is an upper wall
        elif random_wall[0] != 0 and maze[random_wall[0]-1][random_wall[1]] == unvisited and maze[random_wall[0]+1][random_wall[1]] == open_space:
            s_cells = surrounding_cells(random_wall, maze)
            if s_cells < 2:
                # Mark cell as open_space
                maze[random_wall[0]][random_wall[1]] = open_space
                # Handle neighbor operations
                maze, walls = handle_neighbor("up", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("right", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("left", width, height, random_wall, maze, walls)
            walls.remove(random_wall)
            continue

        # Check if wall is bottom wall
        elif random_wall[0] != height-1 and maze[random_wall[0]+1][random_wall[1]] == unvisited and maze[random_wall[0]-1][random_wall[1]] == open_space:
            s_cells = surrounding_cells(random_wall, maze)
            if s_cells < 2:
                # Mark cell as open_space
                maze[random_wall[0]][random_wall[1]] = open_space
                # Handle neighbor operations
                maze, walls = handle_neighbor("down", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("right", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("left", width, height, random_wall, maze, walls)
            walls.remove(random_wall)
            continue

        #Check if wall is a right wall
        elif random_wall[1] != width-1 and maze[random_wall[0]][random_wall[1]+1] == unvisited and maze[random_wall[0]][random_wall[1]-1] == open_space:
            s_cells = surrounding_cells(random_wall, maze)
            if s_cells < 2:
                # Mark cell as open_space
                maze[random_wall[0]][random_wall[1]] = open_space
                # Handle neighbor operations
                maze, walls = handle_neighbor("up", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("right", width, height, random_wall, maze, walls)
                maze, walls = handle_neighbor("down", width, height, random_wall, maze, walls)
            walls.remove(random_wall)
            continue
        else:
            # Delete the wall from the list anyway
            walls.remove(random_wall)
        continue

    # Mark the remaining unvisited cells as walls
    for i in range(height):
        for j in range(width):
            if (maze[i][j] == unvisited):
                maze[i][j] = wall

    # Add starting point
    for i in range(height):
        # 50/50 chance if starting point is top left or top right
        if random.random() < 0.5:
            row = range(width)
        else:
            row = reversed(range(width))
        for j in row:
            if (maze[i][j] == open_space):
                maze[i][j] = start
                break
        # Ensure that nested loop is broken after start is assigned
        else:
            continue
        break

    # Add end point        
    for i in reversed(range(height)):
        # 50/50 chance if end point is top left or top right
        if random.random() < 0.5:
            row = range(width)
        else:
            row = reversed(range(width))
        for j in row:
            if (maze[i][j] == open_space):
                maze[i][j] = goal
                break
        # Ensure that nested loop is broken after start is assigned
        else:
            continue
        break
                
    return maze

if len(sys.argv) == 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    width = 10
    height = 10


maze = generate_maze(width, height)
# Write pat file
text_file = open("test/" + str(width) + "_pat.csp", "w")
text_file.write("#define M " + str(width) + ";\n")
text_file.write("#define N " + str(height)+ ";\n")
text_file.write("var board[N][M] = ")
text_file.write("[%s]" % ", ".join([item for sublist in maze for item in sublist]) +';')
text_file.close()
# Write RL file
text_file = open("mazes/" + str(width) + "_rl.txt", "w")
for sublist in maze:
    text_file.write("%s\n" % "".join(sublist))
text_file.close()
# Visualize maze
print_maze(maze)




