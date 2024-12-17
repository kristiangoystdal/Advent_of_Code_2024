file_path = "Day_11/puzzle_input.txt"
# file_path = "Day_11/test_input.txt"

with open(file_path, "r") as file:
    line = file.read()

lines = line.split(" ")
lines = [int(i) for i in lines]

print(lines)

n = 25

for m in range(n):
    for i in range(len(lines)):
        if lines[i] == 0:
            lines[i] = 1
        elif len(str(lines[i])) % 2 == 0:
            half = len(str(lines[i])) // 2
            first_half = int(str(lines[i])[:half])
            second_half = int(str(lines[i])[half:])
            while str(first_half)[0] == "0":
                first_half = first_half[1:]
            while str(second_half)[0] == 0:
                second_half = second_half[1:]
            lines[i] = first_half
            lines.append(second_half)
            i += 1
        else:
            lines[i] *= 2024
    # print(lines)


print(len(lines))
