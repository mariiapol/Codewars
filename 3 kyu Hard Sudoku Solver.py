def find(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return False
    return True

def check(puzzle, row, column):
    l =puzzle[row]
    l2 = [puzzle[i][column] for i in range(0,9)]
    r  = 3 * (row // 3)
    c = 3 * (column // 3)
    s = [puzzle[i][j] for i in range(r,r + 3) for j in range(c,c +3)]
    numbers = [1,2,3,4,5,6,7,8,9]
    return list(set(numbers) - set(l) -set(l2) - set(s))
 

def min_choice(puzzle):
    min_poss = 10
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                n_poss = len(check(puzzle,r, c))
                if n_poss < min_poss:
                    min_poss = n_poss
                    min_choice = (r, c)
                    if n_poss == 1:
                        return min_choice
    return min_choice


def solve(puzzle):
    #returns the solved puzzle as a 2d array of 9 x 9
    # uses backtracking algorithm to solve the puzzle.
    
    if find(puzzle):
            return puzzle
    else:        
        i, j = min_choice(puzzle)
                 
        for n in check(puzzle, i, j):
            puzzle[i][j] = int(n)

            if solve(puzzle):
                puzzle[i][j] = int(n)
                return puzzle
            else:
                puzzle[i][j] = 0
