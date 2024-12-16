file_path = "Day_10/puzzle_input.txt"
# file_path = "Day_10/test_input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

# print(lines)


def check_adjacent(y, x, lines, current):
    adjacent = []
    if x - 1 >= 0:
        left = lines[y][x - 1]
    else:
        left = "."
    if x + 1 < len(lines[y]):
        right = lines[y][x + 1]
    else:
        right = "."
    if y - 1 >= 0:
        up = lines[y - 1][x]
    else:
        up = "."
    if y + 1 < len(lines):
        down = lines[y + 1][x]
    else:
        down = "."

    # print("Left: ", left)
    # print("Right: ", right)
    # print("Up: ", up)
    # print("Down: ", down)
    try:
        if left != ".":
            if int(left) == current + 1:
                adjacent.append((y, x - 1))
        if right != ".":
            if int(right) == current + 1:
                adjacent.append((y, x + 1))
        if up != ".":
            if int(up) == current + 1:
                adjacent.append((y - 1, x))
        if down != ".":
            if int(down) == current + 1:
                adjacent.append((y + 1, x))

    except IndexError:
        pass
    # print("Adjacent: ", adjacent)
    return adjacent


paths = 0
paths_list = []


def find_path(y, x, lines, current):
    # print("Position: ", y, x)
    global paths, paths_list
    if current == 9:
        # print("Path found")
        paths += 1
        return
    adjacent = check_adjacent(y, x, lines, current)
    if len(adjacent) == 0:
        return
    else:
        for i in adjacent:
            # print(i, current + 1)
            find_path(i[0], i[1], lines, current + 1)


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "0":
            current = 0
            paths_list = []
            y, x = i, j
            find_path(y, x, lines, current)

print(paths)
