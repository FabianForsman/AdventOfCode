
input = open("Day3/input.txt", "r")

data = input.read()

import re

def part1():
    regex = r"mul\(\d+,\d+\)"
    muls = re.findall(regex, data)
    tot = 0
    nr = r"\d+"
    for mul in muls:
        nrs = re.findall(nr, mul)
        tot += int(nrs[0]) * int(nrs[1])
    print(tot)

def part2():
    regex = r"(mul\(\d+,\d+\))+"
    nr = r"\d+"
    do = r"do\(\)"
    dont = r"don't\(\)"
    muls = re.findall(regex, data)
    # find all regexes that are after do() and before don't()

    print(muls)
    for mul in muls:
        nrs = re.findall(nr, mul)

    

#part1()
part2()