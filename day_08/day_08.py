from typing import List
from collections import defaultdict
import itertools

part_one_enabled = False


def part_one():
    frequency_input_map = _read_input()
    antenna_positions = _get_antenna_positions(frequency_input_map)

    return len(_get_antinode_positions(antenna_positions, frequency_input_map))


def _get_antinode_positions(antenna_positions, frequency_map):
    height = len(frequency_map)
    width = len(frequency_map[0])
    
    unique_antinode_positions = set()
    antenna_pair_iterators = []

    print(antenna_positions.values())
    for positions_list in antenna_positions.values():
        antenna_pair_iterators.append(itertools.combinations(positions_list, 2))

    for iter in antenna_pair_iterators:
        for combination in iter:
            pair_one, pair_two = combination
            i,j = pair_one
            x,y = pair_two

            in_bounds = lambda a, limit_h, limit_w: 0<=a[0]<limit_h and 0<=a[1]<limit_w
            
            if part_one_enabled: 
                create_third_pos = lambda i,j,x,y: (x - (i-x), y - (j-y))
                temp = create_third_pos(i,j,x,y)
                if in_bounds(temp, height, width):
                    unique_antinode_positions.add(temp)

                temp = create_third_pos(x,y,i,j)
                if in_bounds(temp, height, width):
                    unique_antinode_positions.add(temp)
            else:
                if pair_one == pair_two:
                    continue
                #print('doing this')
                difference_tuple = lambda a, b: (a[0] - b[0], a[1] - b[1])
                i_inc, j_inc = difference_tuple(pair_one, pair_two)
                temp_i, temp_j = i, j
                temp = (temp_i, temp_j)
                while in_bounds(temp, height, width):
                    print(temp)
                    unique_antinode_positions.add(temp)
                    temp_i = temp_i + i_inc
                    temp_j = temp_j + j_inc
                    temp = (temp_i, temp_j)
                
                temp_i, temp_j = i, j
                temp = (temp_i - i_inc, temp_j - j_inc)
                while in_bounds(temp, height, width):
                    print(str(temp) + "!")
                    unique_antinode_positions.add(temp)
                    print(temp)
                    unique_antinode_positions.add(temp)
                    temp_i = temp_i - i_inc
                    temp_j = temp_j - j_inc
                    temp = (temp_i, temp_j)

    return unique_antinode_positions


def _get_antenna_positions(frequency_map):
    antenna_positions = defaultdict(lambda: [])
    height = len(frequency_map)
    width = len(frequency_map[0])
    for i in range(height):
        for j in range(width):
            curr_char = frequency_map[i][j]
            if curr_char.isdigit() or curr_char.isalpha():
                antenna_positions[curr_char].append((i,j))
    return antenna_positions

def _read_input() -> List[List[str]]:
    arr = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            arr.append([char for char in line])
    return arr

print(part_one())