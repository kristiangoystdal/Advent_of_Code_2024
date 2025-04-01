def calculate_fencing_cost(lines):
    rows, cols = len(lines), len(lines[0])
    visited = [[False] * cols for _ in range(rows)]

    def is_boundary(x, y, char):
        """Check if a given cell (x, y) is part of the perimeter."""
        return x < 0 or x >= rows or y < 0 or y >= cols or lines[x][y] != char

    def dfs(x, y, char):
        """Perform DFS to find the connected region and calculate its area and perimeter."""
        stack = [(x, y)]
        visited[x][y] = True
        area = 0
        perimeter = 0

        while stack:
            cx, cy = stack.pop()
            area += 1
            # Check all four neighbors
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if lines[nx][ny] == char and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                    elif lines[nx][ny] != char:  # Boundary condition
                        perimeter += 1
                else:  # Out of bounds, contributes to perimeter
                    perimeter += 1

        return area, perimeter

    total_cost = 0

    # Loop through all cells to find unvisited regions
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                char = lines[i][j]
                area, perimeter = dfs(i, j, char)
                total_cost += area * perimeter

    return total_cost


# Read input
file_path = "Day_12/puzzle_input.txt"
# file_path = "Day_12/test_input.txt"
with open(file_path, "r") as file:
    lines = file.read().strip().split("\n")

# Solve the problem
total_price = calculate_fencing_cost(lines)
print("Total price of fencing all regions:", total_price)
