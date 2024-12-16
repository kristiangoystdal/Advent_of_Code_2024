# File path for the input
file_path = "Day_9/puzzle_input.txt"
# file_path = "Day_9/test_input.txt"

# Read the disk map input
with open(file_path, "r") as file:
    line = file.read().strip()

# Parse the input into alternating file sizes and free space sizes
disk_map = []
current_id = 0
for i, char in enumerate(line):
    if i % 2 == 0:  # Even indices represent file sizes
        disk_map.append((current_id, int(char)))
        current_id += 1
    else:  # Odd indices represent free space sizes
        disk_map.append((".", int(char)))

# Convert disk_map into the initial disk layout
disk_layout = []
for element, size in disk_map:
    disk_layout.extend([element] * size)


# Function to calculate the checksum of a disk layout
def calculate_checksum(layout):
    checksum = 0
    for position, block in enumerate(layout):
        if isinstance(block, int):  # Only file blocks contribute to checksum
            checksum += position * block
    return checksum


# Compact files according to the new rules
file_blocks = [
    (file_id, size) for file_id, size in disk_map if isinstance(file_id, int)
]
file_blocks.sort(reverse=True)  # Process files in descending order of file ID

for file_id, file_size in file_blocks:
    # print(f"Moving file {file_id} of size {file_size}")
    # Find the leftmost span of free space large enough to fit the file
    free_space_start = -1
    free_space_length = 0

    for i, block in enumerate(disk_layout):
        if block == ".":  # Free space
            if free_space_start == -1:
                free_space_start = i
            free_space_length += 1
        else:  # Encountered a non-free block, reset the span
            free_space_start = -1
            free_space_length = 0

        if free_space_length >= file_size:  # Found a valid span big enough
            # print(f"Found free space at {free_space_start}")
            # print(f"Moving file {file_id} to {free_space_start}")
            # Move the file to the free space
            for j in range(free_space_start, free_space_start + file_size):
                # print(f"Moving block {j} to file {file_id}")
                disk_layout[j] = file_id
                # print(disk_layout[j])

            # Clear the original file location
            blocks_cleared = 0
            for k in range(len(disk_layout) - 1, 0, -1):
                if (
                    disk_layout[k] == file_id
                    and blocks_cleared < file_size
                    and blocks_cleared >= 0
                ):
                    disk_layout[k] = "."
                    blocks_cleared += 1
            break

    # Print the current disk layout
    current_layout = "".join(
        str(block) if isinstance(block, int) else "." for block in disk_layout
    )
    # print(f"Current disk layout: {current_layout}")

# Compute the final checksum
checksum = calculate_checksum(disk_layout)

# Print the resulting layout and checksum
final_layout = "".join(
    str(block) if isinstance(block, int) else "." for block in disk_layout
)
print(f"Final disk layout: {final_layout}")
print(f"The resulting filesystem checksum is: {checksum}")
