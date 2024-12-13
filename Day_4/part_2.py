file_path = "Day_4/puzzle_input.txt"
# file_path = "Day_4/test_input.txt"

with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]


def check_xmas(line, coloum):
    if lines[line][coloum] != "A":  # Center of the X must be "A"
        return 0

    # Define diagonal directions
    d1 = [(1, 1), (-1, -1)]  # Diagonal 1
    d2 = [(1, -1), (-1, 1)]  # Diagonal 2

    def valid_index(row, col):
        return 0 <= row < len(lines) and 0 <= col < len(lines[row])

    try:
        # Check the first diagonal
        diag1 = (
            valid_index(line + d1[0][0], coloum + d1[0][1])
            and valid_index(line + d1[1][0], coloum + d1[1][1])
            and (
                lines[line + d1[0][0]][coloum + d1[0][1]] == "M"
                and lines[line + d1[1][0]][coloum + d1[1][1]] == "S"
                or lines[line + d1[0][0]][coloum + d1[0][1]] == "S"
                and lines[line + d1[1][0]][coloum + d1[1][1]] == "M"
            )
        )

        # Check the second diagonal
        diag2 = (
            valid_index(line + d2[0][0], coloum + d2[0][1])
            and valid_index(line + d2[1][0], coloum + d2[1][1])
            and (
                lines[line + d2[0][0]][coloum + d2[0][1]] == "M"
                and lines[line + d2[1][0]][coloum + d2[1][1]] == "S"
                or lines[line + d2[0][0]][coloum + d2[0][1]] == "S"
                and lines[line + d2[1][0]][coloum + d2[1][1]] == "M"
            )
        )

        return 1 if diag1 and diag2 else 0

    except IndexError:
        return 0


# Count total X-MAS patterns
num = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        num += check_xmas(i, j)

print(num)
