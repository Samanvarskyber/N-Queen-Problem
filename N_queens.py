# Taking number of queens as input from user
print('Enter the number of queens:\t')
N = int(input())

# So here we create a chessboard
# absolutely we create matrix with all element set to 0
board = [[0]*N for _ in range(N)]


def attack(i, j):
    # Checking vertically and horizontally
    for k in range(0, N):
        if board[i][k] == '♛' or board[k][j] == '♛':
            return True
    for k in range(0, N):
        for l in range(0, N):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == '♛':
                    return True
    return False


def N_queens(n):
    if n==0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not(attack(i, j))) and (board[i][j] != '♛'):
                board[i][j] = '♛'
                if N_queens(n-1) == True:
                    return True
                board[i][j] = 0
    return False


N_queens(N)
for i in board:
    print(i)


# arr = [0 for _ in range(5)]
# print(arr)
# ar = [0 for i in range(5)]
# print(ar)
