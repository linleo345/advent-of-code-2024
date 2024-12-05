# day_04


# part 1
from typing import List

XMAS = 'XMAS'

def read_grid() -> List[str]:
    grid = []
    with open('day_04_part_1_input.txt', 'r') as file:
        for line in file:
            grid.append(line.strip())
    return grid

def mini_dfs(pos, hash_set, index, grid, height, width):
    dirs = [(1,0), (1,-1), (1,1), (0,1), (0,-1), (-1, -1), (-1, 0), (-1, 1)]

    num_ways = 0
    for dir in dirs:
        i,j = pos
        i_inc, j_inc = dir
        for index in range(len(XMAS)):
            if not (0<=i<height and 0<=j<width):
                break
            if grid[i][j] != XMAS[index]:
                break
            if index == len(XMAS) - 1:
                num_ways += 1
            i += i_inc
            j += j_inc
    return num_ways

def solve_part_one() -> int:
    grid = read_grid()
    height = len(grid)
    width = len(grid[0])

    xmas_num_ways = 0
    for i in range(height):
        for j in range(width):
            if grid[i][j] == XMAS[0]:
                hash_set = set()
                w = mini_dfs((i,j), hash_set, 0, grid, height, width)
                #print(w)
                xmas_num_ways += w
    return xmas_num_ways


def has_x_mas(pos, grid):
    i,j = pos
    comparison = ["MAS", "SAM"]
    if "".join([grid[i-1][j-1], grid[i][j], grid[i+1][j+1]]) in comparison:
        if "".join([grid[i+1][j-1], grid[i][j], grid[i-1][j+1]]) in comparison:
            return True
    return False

def solve_part_two() -> int:
    grid = read_grid()
    height = len(grid)
    width = len(grid[0])
    xmas_count = 0

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if has_x_mas((i,j), grid):
                xmas_count += 1
    return xmas_count


#print(solve_part_one())
print(solve_part_two())