# Import test input from a .txt file
file_path = "Day_12/test_input.txt"  # Replace with the actual file path

# Read input
with open(file_path, "r") as file:
    grid = file.read().strip().split("\n")

# Directions for movement (right, down, left, up)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def inside_grid(x, y):
    """Check if the position is within the grid."""
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def explore_region(start_x, start_y, plant_type):
    """Explore the region starting from a given cell."""
    stack = [(start_x, start_y)]
    region = set()
    while stack:
        x, y = stack.pop()
        if (x, y) in region:
            continue
        region.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                inside_grid(nx, ny)
                and (nx, ny) not in region
                and grid[nx][ny] == plant_type
            ):
                stack.append((nx, ny))
    return region


def count_sides(region):
    """Count the number of distinct fence sections for a region."""
    print(region)
    sides = 4
    visited_edges = set()  # To avoid double-counting edges
    for x, y in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not inside_grid(nx, ny) or grid[nx][ny] != grid[x][y]:
                # Calculate edge as a pair of sorted coordinates
                edge = tuple(sorted(((x, y), (nx, ny))))
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    sides += 1
    return sides


# Main logic
visited = set()
total_price = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) not in visited:
            # Explore a new region
            plant_type = grid[i][j]
            region = explore_region(i, j, plant_type)

            # Calculate the area and number of sides
            area = len(region)
            sides = count_sides(region)

            # Add price for this region
            total_price += area * sides

            # Mark region as visited
            visited.update(region)

# Output the result
print("Total Price (Part 2):", total_price)
