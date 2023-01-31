class MazeSolver:

    START = 'S'
    END = 'E'
    WALL = 'X'
    BREAD_CRUMB = '.'
    OPEN = ' '

    def __init__(self, maze):
        self.maze = maze
        self.solved = False
        self.number_of_steps = 0
        self.best_solution = None
        self.best_solution_step_count = 0

    def __str__(self):
        return "\n".join(str(row) for row in self.maze) + f"\nSolved in {self.number_of_steps} steps"

    def _can_go(self, row_index, column_index):
        return not ((row_index < 0 or row_index >= len(self.maze)) or
                    (column_index < 0 or column_index >= len(self.maze[row_index])) or
                    (self.maze[row_index][column_index] == MazeSolver.WALL) or
                    (self.maze[row_index][column_index] == MazeSolver.BREAD_CRUMB) or
                    (self.maze[row_index][column_index] == MazeSolver.START))

    def _solve(self, row_index, column_index):
        if self.maze[row_index][column_index] != MazeSolver.START:
            self.number_of_steps += 1

        if self.maze[row_index][column_index] == MazeSolver.END:
           # print("Solution found!")
            #print(self)

            if self.best_solution is None:
                self.best_solution = str(self)
                self.best_solution_step_count = self.number_of_steps
            else:
                if self.best_solution_step_count > self.number_of_steps:
                    self.best_solution_step_count = self.number_of_steps
                    self.best_solution = str(self)

        else:
            if self.maze[row_index][column_index] != MazeSolver.START:
                self.maze[row_index][column_index] = MazeSolver.BREAD_CRUMB
            # up
            if self._can_go(row_index - 1, column_index):
                self._solve(row_index - 1, column_index)
            # down
            if self._can_go(row_index+1, column_index):
                self._solve(row_index+1, column_index)
            # right
            if self._can_go(row_index, column_index+1):
                self._solve(row_index, column_index+1)
            # left
            if self._can_go(row_index, column_index - 1):
                self._solve(row_index, column_index - 1)

            if self.maze[row_index][column_index] != MazeSolver.START:
                self.maze[row_index][column_index] = MazeSolver.OPEN

        self.number_of_steps -= 1

    def solve(self):
        for row_index in range(len(self.maze)):
            for column_index in range(len(self.maze[row_index])):
                if self.maze[row_index][column_index] == MazeSolver.START:
                    self._solve(row_index, column_index)
        if self.best_solution is None:
            raise ValueError("unsolvable maze!")
        return self.best_solution
