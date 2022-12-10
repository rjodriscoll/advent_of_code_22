
prog = open('data.txt').read().split('\n')[:-1]

def parse_instruction(instruction):
    if 'addx' not in instruction:
        return 0
    _, value = instruction.split(' ')
    value = int(value)
    return value


cycles = [20, 60, 100, 140, 180, 220]


def get_values(prog):
    X = 1
    cycle = 0

    values = {}
    for instruction in prog:
        if 'noop' in instruction:
            cycle += 1
            values[cycle] = X
        else:
            for i in range(2):
                cycle += 1
                values[cycle] = X

            X += parse_instruction(instruction)
    return values


def solve_1(values):
    
    return sum([values[v] * v for v in cycles])



def solve_2(values):
    output = ''

    for cycle in range(1, 241):
        if values[cycle] - 1 <= (cycle % 40 - 1) % 40 <= values[cycle] + 1:
            output += '#'
        else:
            output += '.'

    return output

values = get_values(prog)
print(solve_1(values))

stringg = solve_2(values)
substrings = [stringg[i:i+40] for i in range(0, len(stringg), 40)]
for substring in substrings:
    print(substring)