test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def get_lines(use_test_data):
    if(use_test_data):
        lines = test_input.splitlines()
        return lines
    else :
        with open('input.txt') as f:
            lines = f.read().splitlines()
            return lines

def part_1():
    lines = get_lines(False)
    max_size = 100000 
    path = ["/"]
    sizes = {} 

    for l in lines:
        if(l == '$ cd /'):
            path = ["/"]
        elif(l == '$ cd ..' and len(path) > 1):
            path.pop()
        elif(l.startswith('$ cd ')):
            path.append(l[5:])
        elif(l.startswith('$ ls')):
            continue
        elif(l.startswith('dir')):
            continue
        else:
            size = int(l.split()[0])

            for i in range(len(path)-1, -1, -1):
                current_path = '/'.join(path[:i+1]).replace('//', '/')
                current_size = sizes.get(current_path, 0)
                sizes[current_path] = current_size + size
    
    total = 0
    for s in sizes:
        if(sizes[s] < max_size):
            total += sizes[s]

    print("Part 1 --- Total size: {}".format(total))

def part_2():
    max_disc_size = 70000000
    space_needed = 30000000
    lines = get_lines(False)
    path = ["/"]
    sizes = {} 

    for l in lines:
        if(l == '$ cd /'):
            path = ["/"]
        elif(l == '$ cd ..' and len(path) > 1):
            path.pop()
        elif(l.startswith('$ cd ')):
            path.append(l[5:])
        elif(l.startswith('$ ls')):
            continue
        elif(l.startswith('dir')):
            continue
        else:
            size = int(l.split()[0])

            for i in range(len(path)-1, -1, -1):
                current_path = '/'.join(path[:i+1]).replace('//', '/')
                current_size = sizes.get(current_path, 0)
                sizes[current_path] = current_size + size
    
    current_space_used = sizes["/"]
    space_left = max_disc_size - current_space_used
    good_spaces = {}

    for s in sizes:
        if space_left + sizes[s] >= space_needed:
            good_spaces[s] = sizes[s]
    
    good_spaces = sorted(good_spaces.items(), key=lambda x: x[1], reverse=False)

    print(f"Part 2 --- Smallest dir to remove: {good_spaces[0]}")

part_1()
part_2()