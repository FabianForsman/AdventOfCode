input = open("Day4/input.txt", "r")

data = input.read()

# Make data into an m x n matrix array of rows and columns:
data = list(map(list, data.split("\n")))

def part1(word):
    n = len(data)
    m = len(data[0])
    tot = 0
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for x in range(n):
        for y in range(m):
            if data[x][y] == word[0]:
                #print(word[0], "at", (x, y))
                for dir in directions:
                    #print("Direction:", dir)
                    xdir, ydir = dir
                    for i in range(1, len(word)):
                        dx, dy = xdir*i, ydir*i
                        if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
                            break
                        #print("Checking", data[x + dx][y + dy], "at", (x + dx, y + dy))
                        if data[x + dx][y + dy] != word[i]:
                            break
                        if i == len(word) - 1:
                            tot += 1
                            #print("Found", word)                        
    return tot

print(part1("XMAS"))