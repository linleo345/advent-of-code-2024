
part_two = True


def dfs(target, num, index, curr_sum):
    if index == len(num) - 1:
        if target in (curr_sum * num[index], curr_sum + num[index]):
            return True
        elif part_two and target == int(str(curr_sum) + str(num[index])):
            return True
        return False
    
    if index == 0:
        return dfs(target, num, index+1, num[0])
    elif part_two:
        return dfs(target, num, index+1, curr_sum * num[index]) or dfs(target, num, index+1, curr_sum + num[index]) or dfs(target, num, index+1, int(str(curr_sum) + str(num[index])))
    else:
        return dfs(target, num, index+1, curr_sum * num[index]) or dfs(target, num, index+1, curr_sum + num[index])

def part_one():
    equations = _read_input()
    return sum([equation[0] if dfs(equation[0], equation[1:], 0, 0) else 0 for equation in equations])

def _read_input():
    equations = []
    with open('input.txt', 'r') as file:
        for line in file:   
            line = line.strip()
            equations.append([int(line.split(":")[0])])
            for num in line.split(":")[1].strip().split(' '):
                equations[-1].append(int(num))
    return equations

print(part_one())