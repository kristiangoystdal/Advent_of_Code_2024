file_path = "Day_9/puzzle_input.txt"
# file_path = "Day_9/test_input.txt"

with open(file_path, "r") as file:
    line = file.read()


# print(line)
line_list = line.split()
line_list = [char for char in line]
# print(line_list)

new_line = []
dot = False
n = 0
for c in line:
    s = ""
    if c != "0":
        for j in range(int(c)):
            if dot:
                s = "."
            else:
                s = str(n)

            new_line.append(s)
    if not dot:
        n += 1

    dot = not dot

# print()
line = new_line
# print(line)

i = -1
for k in range(len(line)):
    c = line[k]
    if c == "." and k < len(line) + i:

        # print(i, c)
        while line[i] == ".":
            i -= 1

        line[k] = str(line[i])
        line[i] = "."

        # for j in range(len(line)):
        #     print(line[j], end="")
        # print("\n")

# print(line)

tot = 0

for i in range(len(line)):
    if line[i] != ".":
        tot += int(line[i]) * i

print(tot)
