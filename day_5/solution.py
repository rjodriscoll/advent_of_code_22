def get_clean_master_array(arr):
    master_array = []

    for row in reversed(arr):
        start, end = 0, 4
        unpack = []
        while end < len(row) + 4:
            unpack.append(row[start:end].replace(" ", ""))
            start += 4
            end += 4
        master_array.append(unpack)

    return master_array


def get_instruction(string):
    parts = string.split(" ")
    return int(parts[1]), int(parts[3]), int(parts[5])


def extract_top_value(arr, from_loc):
    for i in range(len(arr)):
        if arr[i + 1][from_loc - 1] == "":
            value = arr[i][from_loc - 1]
            arr[i][from_loc - 1] = ""
            return value


def carry_out_instruction(instruction_string, arr, part=1):
    n, from_loc, to_loc = get_instruction(instruction_string)

    # get the available position
    current_height = len(arr)
    values = [extract_top_value(arr, from_loc) for i in range(n)]
    if part == 2:
        values = reversed(values)
    # make space
    if current_height - n < 0 or arr[current_height - n][to_loc - 1] != "":
        [arr.append([""] * 9) for _ in range(n)]

    lowest_free_point = 0
    cell_value = arr[lowest_free_point][to_loc - 1]
    while cell_value != "":
        lowest_free_point += 1
        cell_value = arr[lowest_free_point][to_loc - 1]

    for i in values:
        arr[lowest_free_point][to_loc - 1] = i
        lowest_free_point += 1

    return arr


def solve(part):
    with open("data.txt") as f:
        data = f.read()
    data = data.split("\n")
    arr = data[0:8]
    instructions = data[10:]
    arr = get_clean_master_array(arr)

    for instruction in instructions:
        arr = carry_out_instruction(instruction, arr, part=part)

    num_cols = len(arr[0])
    string = ""
    for col in range(num_cols):
        last_nonempty = -1

        for row in range(len(arr)):
            if arr[row][col] != "":
                last_nonempty = row
        string += arr[last_nonempty][col][1]
    return string


print(solve(part=1))
print(solve(part=2))
