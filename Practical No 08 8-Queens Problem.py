import sys
N = 8
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True
def solve_queen(board, row):
    if row == N:
        print_board(board)
        return True 
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queen(board, row + 1):
                return True
            board[row] = -1 
    return False
def print_board(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
board = [-1] * N
solve_queen(board, 0)
