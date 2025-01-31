input = open("Day3/input.txt", "r")

data = input.read().replace("\n", "")
import re

def part1():
    regex = r"mul\(\d+,\d+\)"
    muls = re.findall(regex, data)
    tot = 0
    nr = r"\d+"
    for mul in muls:
        nrs = re.findall(nr, mul)
        tot += int(nrs[0]) * int(nrs[1])
    return tot

def part2():
    tot = 0
    i = 0
    do = True
    while i < len(data):
        if (data[i:i+4] == "do()"):
            do = True
            #print(data[i:i+4])
            i += 4
        if do and data[i] == "m":
            if data[i+1] == "u" and data[i+2] == "l" and data[i+3] == "(":
                begin = i
                i +=4
                nr1 = ""
                while data[i] in "0123456789":
                    nr1 += data[i]
                    i += 1
                nr2 = ""
                if not data[i] == ",":
                    continue
                i += 1
                while data[i] in "0123456789":
                    nr2 += data[i]
                    i += 1
                #print(data[begin:i+1])
                if data[i] == ")":
                    tot += int(nr1) * int(nr2)
        if data[i:i+7] == "don't()":
            #print(data[i:i+7])
            do = False
            i += 7
        i += 1
    return tot

print(part1())
print(part2())