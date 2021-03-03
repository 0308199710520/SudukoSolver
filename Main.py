grid = [[0, 0, 6, 0, 0, 0, 1, 0, 0],
        [2, 0, 0, 7, 0, 0, 3, 0, 0],
        [0, 5, 3, 0, 0, 0, 0, 4, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 1, 0, 8, 0, 0, 2, 0],
        [8, 0, 0, 0, 0, 0, 0, 9, 4],
        [0, 0, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 6],
        [9, 6, 2, 0, 0, 0, 0, 0, 0]]


def valid(grid, z, y, x):
    # Checks row
    for i in range(9):
        if z == grid[y][i]:
            return False
    # checks col
    for j in range(9):
        if z == grid[j][x]:
            return False

    i0 = y // 3
    j0 = x // 3
    # checks square
    for a in range(3):
        for b in range(3):
            if z == grid[i0 * 3 + a][j0 * 3 + b]:
                return False

    return True


def solver(grid):
    # iterate through every square
    for y in range(9):
        for x in range(9):
            # checks if its an empty position
            if grid[y][x] == 0:
                # checks possible values 1-9
                for z in range(1, 10):
                    # checks if its a possible valid choice
                    if valid(grid, z, y, x):
                        # sets the position equal to the choice if its valid
                        grid[y][x] = z
                        # calls itself recursively with the updated grid
                        solver(grid)
                        # if recursion cannot find the answer(e.g its wrong, the placed numbers is returned to 0
                        # to try another)
                        grid[y][x] = 0
                # returns to previous space if not a valid number, backtracking to the problem value
                return
    # This is only called once each value has been inputted
    for line in grid:
        print(line)


solver(grid)
