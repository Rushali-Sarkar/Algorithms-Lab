def nQueen(n: int) -> [[int]]:

    def makeBoard(n: int) -> [[int]]:
        board = []
        for i in range(n):
            board.append([0 for j in range(n)])
        return board

    def isQueenSafe(board: [[int]], row_number: int, column_number: int, n: int) -> bool:


        for column in range(n):
            if column != column_number and board[row_number][column] == 1:
                return False

        for row in range(n):
            if row != row_number and board[row][column_number] == 1:
                return False

        i = row_number + 1
        j = column_number + 1
        while i < n and j < n:
            if board[i][j] == 1:
                return False
            i += 1
            j += 1

        i = row_number + 1
        j = column_number - 1
        while i < n and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        i = row_number - 1
        j = column_number + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        i = row_number - 1
        j = column_number - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        return True

    def backtrack(row: int) -> bool:

        nonlocal board
        nonlocal n

        if row >= n:
            return True

        for column in range(n):
            if isQueenSafe(board, row, column, n):
                board[row][column] = 1
                if backtrack(row + 1):
                    return True
                board[row][column] = 0
        return False

    board = makeBoard(n)
    if backtrack(0):
        return board
    return [[0]]


    

if __name__ == "__main__":

    print("Enter the value of n")
    n = int(input())
    valid_configuration = nQueen(n)
    if valid_configuration == [[0]]:
        print("Sorry no valid configuration exsists")
    else:
        for each in valid_configuration:
            print(*each)
