with open("data.txt") as f:
    data = f.read()
data = data.split("\n")


DIRECTORY_STACK = [] 

up_dir = '..'


def is_cd(command):
    return '$ cd' in command

def is_ls(command):
    return '$ ls' in command

def get_dir_name(command):
    return command.split(' ')[-1]


def get_ls_results(index):
    contents = []
    for item in data[index + 1 : ]:
        if is_ls(item) or is_cd(item):
            break
        contents.append(item)

    return contents

def parse_contents(contents):
    cont_dict = {}
    for content in contents:
        if content:
            first, second = content.split(' ')
            if first == 'dir':
                cont_dict['/'.join(DIRECTORY_STACK) + '/' + second] = ''
            else:
                cont_dict[second] = int(first)
    return cont_dict

def get_contents_size(dirs, dir_name):
    return sum([v for v in dirs.get(dir_name).values()])

def is_dir(string):
    return string.startswith('/')


dirs = {}

for index, command in enumerate(data):
    if is_cd(command):
        if get_dir_name(command) == up_dir:
            _ = DIRECTORY_STACK.pop()
        else:
            DIRECTORY_STACK.append(get_dir_name(command))
    
    if is_ls(command):
        CURRENT_DIR = '/'.join(DIRECTORY_STACK)
        contents = get_ls_results(index)
        contents = parse_contents(contents)
        dirs[CURRENT_DIR] = contents

def populate_dirs(dirs):
    sorted_keys = sorted(dirs.keys(), key=len, reverse=True)
    for string in sorted_keys:
        for key in dirs.keys():
            if string in [i for i in dirs[key].keys()]:
                dirs[key][string] = get_contents_size(dirs,string)

    return dirs 


dirs = populate_dirs(dirs)

def solve_1(dirs):
    total = 0
    for dir in [k for k in dirs.keys()]:
        size = get_contents_size(dirs,dir)
        if size <= 100000:
            total += size 

    return total

def solve_2(dirs):
    total = 70000000 
    needed  = 30000000
    used = get_contents_size(dirs,'/')
    size_needed = needed -  (total - used)
    possible =[]
    for dir in [k for k in dirs.keys()]:
        size = get_contents_size(dirs,dir)
        if size >= size_needed:
            possible.append(size)

    return min(possible)

print(solve_1(dirs))
print(solve_2(dirs))