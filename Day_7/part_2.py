from itertools import product

file_path = "Day_7/puzzle_input.txt"
# file_path = "Day_7/test_input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    lines = [line.strip() for line in lines]

answer = []
data = []
for line in lines:
    a, d = line.split(":")
    answer.append(a)
    d = d.split(" ")
    data.append(d)

for d in data:
    for i in range(len(d) - 1):
        if d[i] == "":
            d.pop(i)


def evaluate_left_to_right(formula):
    """Evaluates a formula strictly from left to right."""
    tokens = formula.split()
    result = int(tokens[0])  # Start with the first number
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        elif operator == "||":
            result = int(str(result) + str(operand))
        i += 2  # Move to the next operator and operand
    return result


def calculate(data):
    operations = ["+", "*", "||"]
    formulas = []
    # Generate all combinations of operations
    for comb in product(operations, repeat=len(data) - 1):
        # Build the formula strictly left to right
        formula = ""
        for i in range(len(data) - 1):
            formula += data[i] + " " + comb[i] + " "
        formula += data[-1]
        formulas.append(formula)

    # print("Generated formulas (strict left-to-right):", formulas)

    cals = []
    for formula in formulas:
        cals.append(evaluate_left_to_right(formula))

    return cals


tot = 0
for i in range(len(data)):
    result = int(answer[i])
    cals = calculate(data[i])
    # print(cals, result)
    if result in cals:
        tot += result
        # print(result)

print(tot)
