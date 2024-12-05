from enum import Enum
from typing import Dict
from typing import List


def part_one():
    rules = {}
    pages = []

    _read_input_part_one(rules, pages)

    sum_of_middles = 0
    for line in pages:
        if _is_page_valid(rules, line):
            sum_of_middles += int(line[len(line) // 2])
            print(int(line[len(line) // 2]))
    return sum_of_middles

def part_two():
    rules = {}
    pages = []

    _read_input_part_one(rules, pages)

    sum_of_middles = 0
    for line in pages:
        if _is_page_valid(rules, line):
            continue
        else:
            new_arr = _fix_violation_and_return(rules, line)
            sum_of_middles += int(new_arr[len(new_arr) // 2])
            print(new_arr)
            print(int(new_arr[len(new_arr) // 2]))
    return sum_of_middles

def _fix_violation_and_return(rules, line) -> List[str]:
    
    while not _is_page_valid(rules, line):
        new_list = []

        visited = set()
        i = 0
        for i in range(len(line)):
            if i in visited:
                continue

            for j in range(i+1, len(line)):

                if j in visited:
                    continue

                first_page = line[i]
                second_page = line[j]
                if first_page in rules and second_page in rules[first_page]:
                    #if violation
                    # mark as a list
                    # then delete
                    # then make substring of those violations in order, put behind number 
                    new_list.append(second_page)
                    visited.add(j)
            visited.add(i)
            new_list.append(first_page)

        line = new_list
        

    return new_list
            

def _is_page_valid(rules, line):
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            page_before = line[i]
            page_after = line[j]
            if page_before not in rules:
                continue
            if page_after in rules[page_before]:
                return False
    #print("line of pages valid: " + str(line))

    return True



# rules: after -> before
def _read_input_part_one(rules: Dict[str, List[str]], pages: List[List[str]]) -> None:
    class ReadMode(Enum):
        RULES = 1
        PAGES = 2

    read_mode = ReadMode.RULES
    with open('part2.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == "":
                read_mode = ReadMode.PAGES
                continue
            if read_mode == ReadMode.RULES:
                first_int, second_int = line.split("|")
                if second_int in rules:
                    rules[second_int].add(first_int)
                else:
                    rules[second_int] = {first_int}
            if read_mode == ReadMode.PAGES:
                pages.append(line.split(","))
    return

print(part_two())
