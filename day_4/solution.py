def read_text_to_list(file):
    with open(f'{file}') as f:
        data = f.read()
    return data.split('\n')[:-1]


def check_overlap(pair, part):
    a, b = [tuple(map(int, x.split('-'))) for x in pair.split(',')]
    l = list(range(a[0], a[1]+1)), list(range(b[0], b[1]+1))
    sorted_list = sorted(l, key=lambda x: len(x))
    if part == 1:
        return min(sorted_list[0]) in sorted_list[1] and max(sorted_list[0]) in sorted_list[1]
    else:
        return min(sorted_list[0]) in sorted_list[1] or max(sorted_list[0]) in sorted_list[1]


def solve_part_1(data):
    return sum([check_overlap(pair, part=1) for pair in data])


def solve_part_2(data):
    return sum([check_overlap(pair, part=2) for pair in data])


data = read_text_to_list('data.txt')
print(solve_part_1(data))
print(solve_part_2(data))
