from MazeSolver import MazeSolver

def count_down(n):
    if n <= 0:
        print("blastoff!")
    else:
        print(n)
        count_down(n-1)

#count_down(10)

maze = [
    ['S', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', 'X', ' ', ' ', 'E']
]

solver = MazeSolver(maze)
print(solver.solve())