from collections import Counter, deque

file_path = "Day_11/puzzle_input.txt"

# Load data as integers for efficient processing
with open(file_path, "r") as file:
    data = deque(map(int, file.read().split()))  # Use deque for efficient popping

n = 75
batch_size = 1_000_000  # Process 1,000,000 numbers at a time


def process_batch(counter):
    """Process a frequency dictionary of numbers and return the new frequency dictionary."""
    new_counter = Counter()

    # Process all 0s first
    if 0 in counter:
        new_counter[1] += counter[0]  # Replace all 0s with 1

    # Process remaining unique numbers
    for num, count in counter.items():
        if num == 0:
            continue  # Skip 0 since it's already handled

        num_str = str(num)
        num_len = len(num_str)

        if num_len % 2 == 0:  # Even length
            half = num_len // 2
            first_half = int(num_str[:half])
            second_half = int(num_str[half:])

            # Add results to the new counter
            new_counter[first_half] += count
            new_counter[second_half] += count
        else:  # Odd length
            new_counter[num * 2024] += count

    return new_counter


# Perform the iterations with batch processing
for m in range(n):
    counter = Counter()  # Frequency counter for the current iteration

    # Process data in batches
    while data:
        batch = [
            data.popleft() for _ in range(min(batch_size, len(data)))
        ]  # Pop batch-sized chunks
        counter.update(batch)  # Update the counter with batch values

    # Process the frequency counter and collect results
    counter = process_batch(counter)

    # Replace data with the new numbers
    data = deque()
    for num, count in counter.items():
        data.extend([num] * count)

    print(f"Step {m}, len(data): {len(data)}")

print(f"Final length: {len(data)}")
