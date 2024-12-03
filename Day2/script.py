input = open("Day2/input.txt", "r")

data = input.read().split("\n")

# Split the data into a list of lists, where each list is a list of integers
for i in range(len(data)):
    data[i] = list(map(int, data[i].split(" ")))

def part1():
    counter = 0
    for row in data:
        if row == sorted(row) or row == sorted(row, reverse=True):
            if all(1 <= abs(row[j] - row[j + 1]) <= 3 for j in range(len(row) - 1)):
                counter += 1        
    print(counter)

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
    print(counter)

part1()
part2()

input.close()