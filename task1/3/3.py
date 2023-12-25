import math

filename = 'text_3_var_83'
with open(filename) as file:
    lines = file.readlines()

matrix = list()

for line in lines:
    nums = line.strip().split(",")
    for i in range(len(nums)):
        if nums[i] == 'NA':
            nums[i] = str((int(nums[i - 1]) + int(nums[i + 1])) / 2)

    filtered = list(filter(lambda x: math.sqrt(float(x)) > 50+78, nums))
    matrix.append(filtered)

with open('res.txt', 'w') as result:
    for row in matrix:
        for num in row:
            result.write(str(num) + ',')
        result.write("\n")