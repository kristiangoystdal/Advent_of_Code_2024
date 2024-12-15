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

                # print(f"key: {key}, key2: {key2}, value: {value}")
                # print(f"diff x: {diff_x}, diff y: {diff_y}")

                if key[1] < key2[1]:
                    if key[0] < key2[0]:
                        new_key = (key[0] + diff_y, key[1] + diff_x)
                    else:
                        new_key = (key[0] + diff_y, key[1] + diff_x)

                elif key[1] >= key2[1]:
                    if key[0] <= key2[0]:
                        new_key = (key[0] + diff_y, key[1] + diff_x)
                    else:
                        new_key = (key[0] + diff_y, key[1] + diff_x)

                if (
                    new_key[0] >= 0
                    and new_key[1] >= 0
                    and new_key[0] < max_y
                    and new_key[1] < max_x
                ):
                    # print(f"new key: {new_key}")
                    # print("\n")
                    line_list = list(lines[new_key[0]])
                    line_list[new_key[1]] = "#"
                    lines[new_key[0]] = "".join(line_list)

tot = 0
for line in lines:
    tot += line.count("#")
    # print(line)

print(tot)
