def read_all_lines(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        result = []
        for line in lines:
            values = list(map(int, line.split()))
            result.append(values)
        return result


file_path = "Day_2/puzzle_input.txt"
# file_path = "Day_2/test_input.txt"

# Uncomment the following lines to read all lines
reports = read_all_lines(file_path)

num_safe = 0

for report in reports:
    dir = 0
    safe = True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if i == 0:
            if diff < 0:
                dir = -1
            elif diff > 0:
                dir = 1

        if dir == 1:
            if diff < 1 or diff > 3:
                safe = False
                print(report, diff, dir)
                break
        elif dir == -1:
            if diff > -1 or diff < -3:
                safe = False
                print(report, diff, dir)
                break
        else:
            safe = False
            break

    if safe:
        num_safe += 1

print("Number of safe reports: ", num_safe)
