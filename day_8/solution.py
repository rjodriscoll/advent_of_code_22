data = open("data.txt").read()

def solve_1(data):
    n = data.find("\n")
    can_see = 0
    inside = (n - 2) ** 2
    edge_trees = n**2 - inside
    can_see += edge_trees


    forest = [list(map(int, str(row))) for row in data.splitlines()]
    dim = range(1, n - 1)

    for row_index in dim:
        for col_index in dim:

            up = max(col[col_index] for col in forest[:row_index])
            left = max(forest[row_index][:col_index])
            down = max(col[col_index] for col in forest[row_index + 1 :])
            right = max(forest[row_index][col_index + 1 :])

            tree = forest[row_index][col_index]
            if tree > up or tree > down or tree > left or tree > right:
                can_see += 1
    return can_see



def solve_2(data):
    n = data.find("\n")
    forest = [list(map(int, str(row))) for row in data.splitlines()]
    dim = range(1, n - 1)

    total_run_max = 0
    for row_index in dim:
        for col_index in dim:

            tree = forest[row_index][col_index]
            tree

            up = [col[col_index] for col in forest[:row_index]][::-1]
            left = forest[row_index][:col_index][::-1]
            down = [col[col_index] for col in forest[row_index + 1 :]]
            right = forest[row_index][col_index + 1 :]

            values = [up, left, down, right]
            total_run = 1
            for v in values:
                run = 0
                for i in v:
                    if tree > i:
                        run += 1
                    elif tree <= i:
                        run += 1
                        break
                total_run *= run
            if total_run > total_run_max:
                total_run_max = total_run
    return total_run_max

print(solve_1(data))
print(solve_2(data))