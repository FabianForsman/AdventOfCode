input = open("Day2/input.txt", "r")

data = [line for line in input.read().split("\n") if line.strip() != '']

# Split the data into a list of lists, where each list is a list of integers
for i in range(len(data)):
    data[i] = list(map(int, data[i].split(" ")))

def part1():
    counter = 0
    for row in data:
        if row == sorted(row) or row == sorted(row, reverse=True):
            if all(1 <= abs(row[j] - row[j + 1]) <= 3 for j in range(len(row) - 1)):
                counter += 1        
    return counter

def part2():
    counter = 0
    for row in data:
        for idx in range(len(row)):
            item = row[idx]
            item = row.pop(idx)
            if row == sorted(row) or row == sorted(row, reverse=True):
                if all(1 <= abs(row[j] - row[j + 1]) <= 3 for j in range(len(row) - 1)):
                    counter += 1
                    break
            row.insert(idx, item) 
    return counter

print(part1())
print(part2())