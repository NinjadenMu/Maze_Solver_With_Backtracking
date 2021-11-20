from tkinter import *
import solver
import time

def submit():
    global dimensions
    dimensions = entry.get()

    if dimensions != '':
        try:
            dimensions = int(dimensions)
            root.destroy()

        except:
            Label(root, text = 'Please enter a valid input! ').pack()

    else:
        Label(root, text = 'Please enter the desired dimension! ').pack()
    
root = Tk()
root.title('Select Maze Dimensions')

instructions = Label(root, text = 'Input dimensions here (will create N x N maze): ')
entry = Entry(root)
submit_button = Button(root, text = 'Submit', command = submit)

instructions.pack()
entry.pack()
submit_button.pack()

root.mainloop()


def convert_buttons_to_data(maze):
    output = []
    for square in maze:
        if square['bg'] == '#D3D3D3' or square['bg'] == '#87ceeb':
            output.append(1)

        else:
            output.append(0)

    return output

def visualize_solve(solution):
    global root
    step = 1
    for node in solution:
        root.after(200)
        maze[node]['bg'] = 'green'
        maze[node]['text'] = step
        step += 1
        root.update()

def init_solve():
    global solution
    connections_matrix = [[] for i in range(dimensions ** 2)]
    maze_data = convert_buttons_to_data(maze)

    for i in range(len(maze_data)):
        if i // dimensions > 0 and maze_data[i] == 1 and maze_data[i - dimensions] == 1:
            connections_matrix[i].append((i, i - dimensions))

        if i // dimensions < (dimensions - 1) and maze_data[i] == 1 and maze_data[i + dimensions] == 1:
            connections_matrix[i].append((i, i + dimensions))

        if i % dimensions > 0 and maze_data[i] == 1 and maze_data[i - 1] == 1:
            connections_matrix[i].append((i, i - 1))

        if i % dimensions < (dimensions - 1) and maze_data[i] == 1 and maze_data[i + 1] == 1:
            connections_matrix[i].append((i, i + 1))

    solution = solver.solver(connections_matrix)
    visualize_solve(solution)
    return solution
        
def toggle_wall(loc):
    global maze
    global root

    if maze[loc].cget('bg') == '#D3D3D3':
        maze[loc]['bg'] = '#8b0000'
        maze[loc]['text'] = '|'

    else:
        maze[loc]['bg'] = '#D3D3D3'
        maze[loc]['text'] = ''

root = Tk()
root.title("Click on blocks to make walls.  When you're done, click solve!")

maze = []

for loc in range(dimensions ** 2):
    b = Button(root, height = 6, width = 12, text = '', bg = '#D3D3D3', command = lambda loc = loc: toggle_wall(loc))
    maze.append(b)

maze[0]['bg'] = '#87ceeb'
maze[0]['text'] = 'Start'
maze[-1]['bg'] = '#87ceeb'
maze[-1]['text'] = 'End'


for i in range(len(maze)):
    maze[i].grid(row = int(i / dimensions) + 1, column = i % dimensions)

solve_button = Button(root, text = 'Solve!', command = init_solve)
solve_button.grid(row = dimensions + 1, column = dimensions // 2)
root.mainloop()
