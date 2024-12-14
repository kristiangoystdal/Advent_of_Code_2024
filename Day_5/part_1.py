file_path = "Day_5/puzzle_input.txt"
# file_path = "Day_5/test_input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    lines = [line.strip() for line in lines]
    split_lines = []
    for line in lines:
        split_lines.extend(line.split("\n"))
    lines = split_lines

    rules = []
    orders = []
    temp = []
    for l in lines:
        if l == "":
            rules = temp
            temp = []
        else:
            if "|" in l:
                temp.append(l.split("|"))
            elif "," in l:
                temp.append(l.split(","))

    orders = temp

# print(rules)
# print(orders[0])


def check_order(order, rules):
    # print(order)
    for o in order:
        for r in rules:
            if o in r:
                try:
                    if r.index(o) == 0:
                        if r[1] in order:
                            if order.index(r[0]) > order.index(r[1]):
                                # print(r, order)
                                return 0
                except:
                    pass

    return int(order[int((len(order) - 1) / 2)])


num = 0
for order in orders:
    num += check_order(order, rules)

print(num)
