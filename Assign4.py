# BACKTRACKING

#Number of queens
print ("Enter the number of queens")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def nQueen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion
                #wether we can put the next queen with this arrangment or not
                if nQueen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

stat = nQueen(N)

if stat == True:
    for i in board:
        print (i)

else:
    print("No result possible")

#____________________

#BRANCH AND BOUND

def isSafe_BnB(board,row, col, column, slash, backslash):
    if column[col] or slash[row+col] or backslash[row-col+len(board)-1]:
        return False
    return True

def setArrays(row, col, column, slash, backslash):
    column[col] = 1
    slash[row+col] = 1
    backslash[row-col+len(column)-1] = 1


def branchAndBound(board, row, col_arr, slash, backslash):
    if row==len(board):
        for i in board:
            for j in i:
                print(j, end=" ")
            print()
        return True
    for col in range(len(board[0])):
        if isSafe_BnB(board, row, col, col_arr, slash, backslash):
            setArrays(row, col, col_arr, slash, backslash)
            board[row][col]=1
            if not branchAndBound(board, row+1, col_arr, slash, backslash):
                col_arr[col] = 0
                board[row][col]=0
                slash[row+col] = 0
                backslash[row-col+len(col_arr)-1] = 0
            # print(slash, backslash, col_arr)



col_arr = [0 for i in range(len(board))]
slash = [0 for i in range(2*len(board)-1)]
backslash = [0 for i in range(2*len(board)-1)]
branchAndBound(board, 0, col_arr, slash, backslash)
