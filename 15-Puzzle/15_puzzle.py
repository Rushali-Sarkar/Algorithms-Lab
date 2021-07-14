def isSolvable(grid: [[int]], n: int) -> bool:

    all_coordinates = []
    for i in range(n):
        for j in range(n):
            all_coordinates.append([i, j])


    inversion_count = 0
    for i in range(len(all_coordinates)):
        x, y = all_coordinates[i]
        if grid[x][y] == 0:
            continue
        for j in range(i + 1, len(all_coordinates)):
            dx, dy = all_coordinates[j]
            if grid[dx][dy] == 0:
                continue
            elif grid[x][y] > grid[dx][dy]:
                inversion_count+= 1

    def rowCount(grid: [[int]], n: int) -> int:
        row_count = 0
        for i in range(n - 1, -1, -1):
            row_count += 1
            for j in range(n):
                if grid[i][j] == 0:
                    return row_count
        return -1

    if n % 2 == 1:
        return inversion_count % 2 == 0

    row_count = rowCount(grid, n)
    return (row_count % 2 == 0 and inversion_count % 2 == 1) or (row_count % 2 == 1 and inversion_count % 2 == 0)



if __name__ == "__main__":

    print("Enter the number of rows")
    n = int(input())
    print("Enter the grid row wise, use 0 for the blank space")
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    if isSolvable(grid, n):
        print("Yes the grid is solveable")
    else:
        print("No the grid is not solveable")

