
def read_text_to_list(file):
    with open(f'{file}') as f:
        data = f.read()
    return data.split('\n')[:-1]


def split_in_two(string):
    half = len(string)//2
    return string[:half], string[half:]


def find_duplicates(string_1, string_2, string_3=None):
    s1s2_common = set(string_1).intersection(set(string_2))
    if string_3:
        return list(s1s2_common.intersection(set(string_3)))[0]
    return list(s1s2_common)[0]


def get_alphabet_index(character):
    alphabet_index = ord(character.lower()) - ord('a')
    return alphabet_index + 1 if character.islower() else alphabet_index + 27


def get_priority(string):
    s1, s2 = split_in_two(string=string)
    char = find_duplicates(s1, s2)
    return get_alphabet_index(char)


def solve_part_1(data):
    tally = 0
    for rucksack in data:
        tally += get_priority(rucksack)
    return tally


def solve_part_2(data):
    tally = 0
    start, finish = 0, 3

    while finish <= len(data):
        batch = data[start: finish]

        char = find_duplicates(batch[0], batch[1], batch[2])
        tally += get_alphabet_index(char)
        start, finish = start + 3, finish + 3
    return tally

