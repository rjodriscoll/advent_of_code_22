def read_text(file):
    with open(f'day_1/{file}') as f:
        return f.read()

def get_text_as_list(file: str):
    return read_text(file).splitlines()

def find_gaps_in_list(data):
    gaps = [i for i, x in enumerate(data) if x == '']
    return gaps
    
def get_sums(data):
    gaps = find_gaps_in_list(data)
    sub_lists = [data[i:j] for i, j in zip([0] + gaps, gaps + [None])]
    sums = [sum([int(i) for i in v if i != '']) for i, v in enumerate(sub_lists)]
    return sums

def get_sum_n_largest_values_in_list(data, n):
    sums = get_sums(data)
    return sum(sorted(sums, reverse=True)[:n])


data = get_text_as_list('data.txt')

print(get_sum_n_largest_values_in_list(data, 3))


