class CheckersSolver:

    WHITE = 'W'
    BLACK = 'B'
    EMPTY = ' '

    def __init__(self, board):
        self._board = board
        self._current_jumps = 0
        self._current_max_jumps = 0
        self._jump_lengths = []

        if len(board) != 8:
            raise ValueError("Invalid board size")
        for row in board:
            if len(row) != 8:
                raise ValueError("Invalid board size")

        should_be_odd = None

        for row in board:
            for column_index in range(len(row)):
                if row[column_index] != ' ':
                    if should_be_odd is None:
                        # even numbers will be 0 which is false
                        # odd numbers will be 1 which is true
                        should_be_odd = column_index % 2
                    elif should_be_odd:
                        if column_index % 2 is False: # even number index
                            raise ValueError("invalid board setup")
                    else: # should be even
                        if column_index % 2: # odd number index
                            raise ValueError("invalid board setup")
            if should_be_odd is not None:
                should_be_odd = not should_be_odd

    def get_max_jumps(self):

        for row_index in range(len(self._board)):
            for column_index in range(len(self._board[row_index])):
                if self._board[row_index][column_index] == self.WHITE:
                    self._current_max_jumps = 0
                    self._get_max_jumps(row_index, column_index)
        if len(self._jump_lengths) == 0:
            return 0
        return max(self._jump_lengths)

    def _can_jump(self, row_index, column_index, row_modifier, column_modifier):
        return 0 <= row_index + row_modifier < len(self._board) and \
            0 <= column_index + column_modifier < len(self._board[row_index]) and \
            self._board[row_index+row_modifier//2][column_index+column_modifier//2] == self.BLACK and \
            self._board[row_index+row_modifier][column_index+column_modifier] == self.EMPTY

    def _try_jump(self, row_index, column_index, row_modifier, column_modifier):
        if self._can_jump(row_index, column_index, row_modifier, column_modifier):
            self._current_jumps += 1
            self._board[row_index][column_index] = self.EMPTY
            self._board[row_index + row_modifier//2][column_index+ column_modifier//2] = self.EMPTY
            self._board[row_index + row_modifier][column_index + column_modifier] = self.WHITE
            self._get_max_jumps(row_index+ row_modifier, column_index+column_modifier)
            self._board[row_index + row_modifier][column_index + column_modifier] = self.EMPTY
            self._board[row_index + row_modifier//2][column_index + column_modifier//2] = self.BLACK
            self._board[row_index][column_index] = self.WHITE
            self._current_jumps -= 1

    def _get_max_jumps(self, row_index, column_index):
        if self._current_jumps > self._current_max_jumps:
            self._current_max_jumps = self._current_jumps
            self._jump_lengths.append(self._current_max_jumps)
        # up left
        self._try_jump(row_index, column_index, -2, -2)
        # up right
        self._try_jump(row_index, column_index, -2, 2)
        # down left
        self._try_jump(row_index, column_index, 2, -2)
        # down right
        self._try_jump(row_index, column_index, 2, 2)

