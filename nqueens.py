def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_safe(board, row, col, n):
    #Check this column on upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    #Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if j<0:
            break
        if board[i][j] == 'Q':
            return False

    #Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if j>=n:
            break
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row>=n:
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q' #Place queen
            solve_n_queens_util(board, row+1, n) #Recur to place the rest
            board[row][col] = '.' #backtrack

def solve_n_queens(n, first_queen_position):
    board = [['.' for _ in range(n)] for _ in range(n)]
    row, col = first_queen_position
    board[row][col] = 'Q' #Place the first queen
    solve_n_queens_util(board, row+1, n) #Start from the next row

n = 4
first_queen_position = (0,1) #Place the first queen at row 0, column 1
solve_n_queens(n, first_queen_position)