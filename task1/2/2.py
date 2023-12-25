filename = 'text_2_var_83'
with open(filename) as file:
    lines = file.readlines()

sum_lines = list()

for line in lines:
    nums = line.split("|")
    sum_line = 0
    for num in nums:
        num.replace("\n", "")
        sum_line += int(num)

    sum_lines.append(sum_line)

with open('text_2_var_78_result.txt', 'w') as result:
    for value in sum_lines:
        result.write(str(value) + "\n")