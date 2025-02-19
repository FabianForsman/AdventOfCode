input = open("Day5/input.txt", "r")

data = input.read()

# Split data into two parts, split by an empty line:
data = data.split("\n")

# Split the first part of the data and the second part. They are separated by an empty element:
for i in range(len(data)):
    data[i] = data[i].split("\n")

conditions = []
orders = []
i = 0
while data[i] != [""]:
    data[i] = list(map(int, data[i][0].split("|")))
    conditions.append(data[i])
    i += 1
for j in range(i + 1, len(data)):
    data[j] = list(map(int, data[j][0].split(',')))
    orders.append(data[j])
    
def part1():
    for order_idx in range(len(orders)):
        order = orders[order_idx]

def part2():
    pass

part1()
part2()