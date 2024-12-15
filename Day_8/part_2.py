file_path = "Day_8/puzzle_input.txt"
# file_path = "Day_8/test_input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    lines = [line.strip() for line in lines]

max_x = len(lines[0])
max_y = len(lines)

dict = {}
for l in range(len(lines)):
    for c in range(len(lines[l])):
        if lines[l][c] != ".":
            dict[(l, c)] = lines[l][c]


for key, value in dict.items():
    for key2, value2 in dict.items():
        if key != key2:
            if value == value2:
                diff_x = key[1] - key2[1]
                diff_y = key[0] - key2[0]
                k = 0
                x = diff_x
                y = diff_y
                while True:
                    if (
                        key[0] + y < 0
                        or key[1] + x < 0
                        or key[0] + y >= max_y
                        or key[1] + x >= max_x
                    ):
                        break

                    if key[1] < key2[1]:
                        if key[0] < key2[0]:
                            new_key = (key[0] + y, key[1] + x)
                        else:
                            new_key = (key[0] + y, key[1] + x)
                    elif key[1] >= key2[1]:
                        if key[0] <= key2[0]:
                            new_key = (key[0] + y, key[1] + x)
                        else:
                            new_key = (key[0] + y, key[1] + x)

                    if (
                        new_key[0] >= 0
                        and new_key[1] >= 0
                        and new_key[0] < max_y
                        and new_key[1] < max_x
                    ):
                        if (
                            lines[new_key[0]][new_key[1]] == "."
                            or lines[new_key[0]][new_key[1]] == "#"
                        ):
                            line_list = list(lines[new_key[0]])
                            line_list[new_key[1]] = "#"
                            lines[new_key[0]] = "".join(line_list)

                    x += diff_x
                    y += diff_y

tot = 0
for line in lines:
    for c in range(len(line)):
        if line[c] != ".":
            tot += 1
    print(line)

print(tot)
