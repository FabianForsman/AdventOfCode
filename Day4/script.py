import numpy as np
from math import pi

input = open("Day4/input.txt", "r")
#input = open("test_data.txt", "r")
data = input.read()
data = list(map(list, data.split("\n")))

def part1(word):
    n = len(data)
    m = len(data[0])
    tot = 0
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for x in range(n):
        for y in range(m):
            if data[x][y] == word[0]:
                for dir in directions:
                    xdir, ydir = dir
                    for i in range(1, len(word)):
                        dx, dy = xdir*i, ydir*i
                        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
                            break
                        if data[x + dx][y + dy] != word[i]:
                            break
                        if i == len(word) - 1:
                            tot += 1
    return tot

def part2(word):
    if len(word) % 2 != 1:
        return 0
    middle_idx = len(word) // 2
    middle_char = word[middle_idx]
    m = len(data)
    n = len(data[0])
    tot = 0
    directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    for x in range(0, n):
        for y in range(0, m):
            if data[x][y] == middle_char:
                stop = False
                for k in range(1, middle_idx + 1):
                    next_char = word[middle_idx + k]
                    prev_char = word[middle_idx - k]
                    if stop: break
                    for xdir1, ydir1 in directions:
                        if stop: break
                        for xdir2, ydir2 in directions:
                            if (xdir1, ydir1) == (xdir2, ydir2) or (xdir1, ydir1) == (-xdir2, -ydir2):
                                continue
                            dx1, dy1 = xdir1 * k, ydir1 * k
                            dx2, dy2 = xdir2 * k, ydir2 * k
                            x1, y1 = x + dx1, y + dy1
                            x2, y2 = x + dx2, y + dy2
                            if not (0 <= x1 < n and 0 <= y1 < m and 0 <= x2 < n and 0 <= y2 < m):
                                break
                            char1, char2 = data[x1][y1], data[x2][y2]
                            if char1 != char2 or (char1 != next_char and char1 != prev_char):
                                break
                            opp_x1, opp_y1 = x1 - 2 * dx1, y1 - 2 * dy1
                            opp_x2, opp_y2 = x2 - 2 * dx2, y2 - 2 * dy2
                            if not (0 <= opp_x1 < n and 0 <= opp_y1 < m and 0 <= opp_x2 < n and 0 <= opp_y2 < m):
                                break
                            opp_char1, opp_char2 = data[opp_x1][opp_y1], data[opp_x2][opp_y2]
                            if opp_char1 != opp_char2 or (opp_char1 != next_char and opp_char1 != prev_char) or char1 == opp_char1:
                                break
                            if k == middle_idx:
                                stop = True
                                tot += 1
    return tot

print(part1("XMAS"))
print(part2("MAS"))