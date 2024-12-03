
input = open("Day1/input.txt", "r")

data = input.read().split("\n")

left = []
right = []
for row in data:
    left.append(int(row[:row.find(" ")]))
    right.append(int(row[row.find(" "):].strip()))

def part1():
    left.sort()
    right.sort()

    dist = 0
    for i in range(len(left)):
        dist += abs(left[i] - right[i])
    print(dist)

def part2():
    left.sort()
    right.sort()
    checked_nrs = []
    for i in range(len(left)):
        cnt = 0
        for j in range(len(right)):
            if left[i] == right[j]:
                cnt += 1
        checked_nrs.append((left[i], cnt))
    
    tot = 0
    for nr in checked_nrs:
        tot += nr[0] * nr[1]
    print(tot)
part1()
part2()
