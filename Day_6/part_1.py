file_path = "Day_6/puzzle_input.txt"
# file_path = "Day_6/test_input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    lines = [list(line.strip()) for line in lines]


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("\n")


def endgame():
    print("ENDGAME")
    print_matrix(lines)
    x_count = sum(row.count("X") for row in lines)
    print(f"Count of 'X': {x_count+1}")
    exit()


def check_front(x, y):
    try:
        if lines[y][x] != "#":
            return True
        else:
            return False
    except IndexError:
        endgame()


print_matrix(["".join(line) for line in lines])


def move(x, y):
    if lines[y][x] == "^":
        if check_front(x, y - 1):
            lines[y][x] = "X"
            return x, y - 1
        else:
            return -1, -1
    elif lines[y][x] == ">":
        if check_front(x + 1, y):
            lines[y][x] = "X"
            return x + 1, y
        else:
            return -1, -1
    elif lines[y][x] == "v":
        if check_front(x, y + 1):
            lines[y][x] = "X"
            return x, y + 1
        else:
            return -1, -1
    elif lines[y][x] == "<":
        if check_front(x - 1, y):
            lines[y][x] = "X"
            return x - 1, y
        else:
            return -1, -1
    return -1, -1


for l in lines:
    if "^" in l:
        x = l.index("^")
        y = lines.index(l)
        break

player = "^"

dir = ["^", ">", "v", "<"]
dirIndex = 0

while True:
    prev_x = x
    prev_y = y
    x, y = move(x, y)
    if x == -1:
        dirIndex += 1
        player = dir[dirIndex % 4]
        lines[prev_y][prev_x] = player
        # print(player)
        x, y = prev_x, prev_y
    # print(x, y)
    lines[y][x] = player
    # print_matrix(lines)
    # input()
c
