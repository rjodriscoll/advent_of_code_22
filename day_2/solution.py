def read_text(file):
    with open(f'{file}') as f:
        return f.read()


WIN = 6
DRAW = 3
LOSE = 0
PAPER = 2
ROCK = 1
SCISSORS = 3

mapping = {
    'A': {'Y': {WIN: PAPER},
          'X': {DRAW: ROCK},
          'Z': {LOSE: SCISSORS}
          },
    'B': {'Y': {DRAW: PAPER},
          'X': {LOSE: ROCK},
          'Z': {WIN: SCISSORS}},
    'C': {'Y': {LOSE: PAPER},
          'X': {WIN: ROCK},
          'Z': {DRAW: SCISSORS}}

}


def return_first(data):

    tally = 0
    for i in data:

        tally += [(k + v) for k, v in mapping.get(i.split(' ')
                                                  [0]).get(i.split(' ')[1]).items()][0]

    return tally


def return_second(data):
    required = {
        'Y': DRAW,
        'X': LOSE,
        'Z': WIN
    }
    tally = 0
    for i in data:
        value_needed = required.get(i.split(' ')[1])

        to_search = mapping.get(i.split(' ')[0])

        pairs = to_search.values()
        for pair in pairs:
            if value_needed in pair.keys():
                tally += list(pair.keys())[0] + list(pair.values())[0]

    return tally


data = read_text('data.txt')

data = data.split('\n')[:-1]


print(return_first(data))

print(return_second(data))
