file_path = "Day_4/puzzle_input.txt"
# file_path = "Day_4/test_input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    lines = [line.strip() for line in lines]


def check_xmas(line, coloum):
    found = 0
    if coloum + 3 < len(lines[line]):
        if lines[line][coloum] == "X":
            if lines[line][coloum + 1] == "M":
                if lines[line][coloum + 2] == "A":
                    if lines[line][coloum + 3] == "S":
                        found += 1

    if coloum - 3 >= 0:
        if lines[line][coloum] == "X":
            if lines[line][coloum - 1] == "M":
                if lines[line][coloum - 2] == "A":
                    if lines[line][coloum - 3] == "S":
                        found += 1

    if line + 3 < len(lines):
        if lines[line][coloum] == "X":
            if lines[line + 1][coloum] == "M":
                if lines[line + 2][coloum] == "A":
                    if lines[line + 3][coloum] == "S":
                        found += 1

    if line - 3 >= 0:
        if lines[line][coloum] == "X":
            if lines[line - 1][coloum] == "M":
                if lines[line - 2][coloum] == "A":
                    if lines[line - 3][coloum] == "S":
                        found += 1

    if line + 3 < len(lines) and coloum + 3 < len(lines[line]):
        if lines[line][coloum] == "X":
            if lines[line + 1][coloum + 1] == "M":
                if lines[line + 2][coloum + 2] == "A":
                    if lines[line + 3][coloum + 3] == "S":
                        found += 1

    if line - 3 >= 0 and coloum - 3 >= 0:
        if lines[line][coloum] == "X":
            if lines[line - 1][coloum - 1] == "M":
                if lines[line - 2][coloum - 2] == "A":
                    if lines[line - 3][coloum - 3] == "S":
                        found += 1

    if line + 3 < len(lines) and coloum - 3 >= 0:
        if lines[line][coloum] == "X":
            if lines[line + 1][coloum - 1] == "M":
                if lines[line + 2][coloum - 2] == "A":
                    if lines[line + 3][coloum - 3] == "S":
                        found += 1

    if line - 3 >= 0 and coloum + 3 < len(lines[line]):
        if lines[line][coloum] == "X":
            if lines[line - 1][coloum + 1] == "M":
                if lines[line - 2][coloum + 2] == "A":
                    if lines[line - 3][coloum + 3] == "S":
                        found += 1

    return found


num = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        num += check_xmas(i, j)


print(num)
