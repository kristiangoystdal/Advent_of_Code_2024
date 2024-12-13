def read_first_line(file_path):
    with open(file_path, "r") as file:
        first_line = file.readline().strip()
        values = list(map(int, first_line.split()))
        return values


def read_all_lines(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        first_column = []
        second_column = []
        for line in lines:
            values = list(map(int, line.strip().split()))
            if len(values) >= 2:
                first_column.append(values[0])
                second_column.append(values[1])
        return first_column, second_column


file_path = "Day_1/puzzle_input.txt"

# Uncomment the following lines to read all lines
first_column, second_column = read_all_lines(file_path)

first_column.sort()
second_column.sort()

tot = 0
for i in range(len(first_column)):
    tot += abs(first_column[i] - second_column[i])

print(tot)
