# file_path = "Day_6/puzzle_input.txt"
file_path = "Day_6/test_input.txt"

with open(file_path, "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))
    print("\n")


def find_guard_position(lines):
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell in "^>v<":  # Guard's starting position
                return x, y, cell
    return None, None, None


def move(x, y, direction):
    if direction == "^":
        return x, y - 1
    elif direction == ">":
        return x + 1, y
    elif direction == "v":
        return x, y + 1
    elif direction == "<":
        return x - 1, y
    return x, y


def is_valid_position(lines, x, y):
    return 0 <= y < len(lines) and 0 <= x < len(lines[0]) and lines[y][x] != "#"


def simulate_with_obstruction(lines, obstruction_x, obstruction_y):
    # Copy grid to simulate the obstruction
    grid = [row[:] for row in lines]
    grid[obstruction_y][obstruction_x] = "O"

    # Find the guard's starting position and direction
    x, y, direction = find_guard_position(grid)
    if x is None or y is None:
        return False

    visited = set()
    while True:
        if (x, y, direction) in visited:
            return True  # Guard is stuck in a loop
        visited.add((x, y, direction))

        next_x, next_y = move(x, y, direction)
        if not is_valid_position(grid, next_x, next_y):
            # Change direction clockwise if blocked
            direction = {"^": ">", ">": "v", "v": "<", "<": "^"}[direction]
        else:
            x, y = next_x, next_y

        # Guard hits the obstruction
        if grid[y][x] == "O":
            return False


# Find all potential positions for an obstruction
def find_obstruction_positions(lines):
    positions = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == ".":
                positions.append((x, y))
    return positions


# Main simulation
obstruction_positions = find_obstruction_positions(lines)
valid_positions = 0

for x, y in obstruction_positions:
    if simulate_with_obstruction(lines, x, y):
        valid_positions += 1

print(f"Number of valid obstruction positions: {valid_positions}")
