def find(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i,j
    return None

def check(puzzle, n, row, column):
    if n in puzzle[row]:
        return False
    if n in [puzzle[i][column] for i in range(0,9)]:
        return False
    r  = 3 * (row // 3)
    c = 3 * (column // 3)
    if n in [puzzle[i][j] for i in range(r,r + 3) for j in range(c,c +3)]:
        return False
    return True
    
def sudoku(puzzle):
    #returns the solved puzzle as a 2d array of 9 x 9
    # uses simple backtracking algorithm to solve the puzzle.
    
    if find(puzzle) == None:
            return puzzle
    else:
        i,j = find(puzzle)
    for n in range(1,10):
        if check(puzzle, n, i, j):
            puzzle[i][j] = n

            if sudoku(puzzle):
                puzzle[i][j] = n
                return puzzle
            else:
                puzzle[i][j] = 0
