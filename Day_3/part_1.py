file_path = "Day_3/puzzle_input.txt"
# file_path = "Day_3/test_input.txt"

with open(file_path, "r") as file:
    str = file.read()

tot = 0
for i in range(len(str)):
    skip = False
    if str[i] == "m":
        if str[i + 1] == "u":
            if str[i + 2] == "l":
                if str[i + 3] == "(":
                    j = 0
                    num1 = ""
                    while str[i + 4 + j] != ",":
                        if str[i + 4 + j].isdigit():
                            num1 += str[i + 4 + j]
                            j += 1
                        else:
                            num1 = ""
                            skip = True
                            break

                    if skip == False:
                        num2 = ""
                        skip = False
                        j += 1
                        while str[i + 4 + j] != ")":
                            if str[i + 4 + j].isdigit():
                                num2 += str[i + 4 + j]
                                j += 1
                            else:
                                num1 = ""
                                num2 = ""
                                skip = True
                                break

                    if skip == False:
                        tot += int(num1) * int(num2)

print(tot)
