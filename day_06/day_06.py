from typing import List
from enum import Enum

class Direction(Enum):
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4
    
directions = {Direction.LEFT: (0, -1), Direction.RIGHT: (0, 1), Direction.UP: (-1, 0), Direction.DOWN: (1, 0)}

turn_direction = {
    Direction.LEFT: Direction.UP, 
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT
}


def part_two():
    map = []
    read_map_input_into_array(map)
    start_i, start_j = get_starting_position(map)

    possible_obstruction_coords = get_visited_coords(map, start_i, start_j)

    ways_to_loop = 0

    tries = 0

    for i, j in possible_obstruction_coords:
        if (i,j) == (start_i, start_j):
            continue
        if map[i][j] == '#':
            continue
        map[i][j] = '#'
        if len(get_visited_coords(map, start_i, start_j)) == 0:
            ways_to_loop += 1
        map[i][j] = '.'
        tries += 1
        print(tries)
    return ways_to_loop

def part1():
    map = []
    read_map_input_into_array(map)
    i,j = get_starting_position(map)
    return len(get_visited_coords(map, i, j))


def get_visited_coords(map, i, j):
    visited_coords = set()

    turning_coords = set()

    curr_dir = Direction.UP

    steps = 0

    while True:
        #print(str(i) + " " + str(j))
        visited_coords.add((i,j))
        steps += 1
        i_net, j_net = directions[curr_dir]
        next_i = i + i_net
        next_j = j + j_net
        
        if not ( 0 <= next_i < len(map) and 0 <= next_j < len(map[0]) ):
            
            #print(steps)
            break

        if map[next_i][next_j] == '#':
            curr_dir = turn_direction[curr_dir]
            if (next_i, next_j, curr_dir) in turning_coords:
                return set()
            turning_coords.add((next_i, next_j, curr_dir))
        else:
            i = next_i
            j = next_j
    return visited_coords

def get_starting_position(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                return (i,j)

def read_map_input_into_array(arr) -> List[str]:
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            arr.append([c for c in line])

print(part_two())