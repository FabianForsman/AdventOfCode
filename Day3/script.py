import os
input = open("Day3/input.txt", "r")

data = input.read()
data = data.replace("\n", "")

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
    mul = r"(mul\(\d+,\d+\))+"
    nr = r"\d+"
    do = r"do\(\)"
    dont = r"don't\(\)"
    first_regexs = r"(mul\(\d+,\d+\).*?)+(don't\(\))"
    regex = r"(do\(\)).*?(mul\(\d+,\d+\).*?)+(don't\(\))(.*?)"
    matches = re.finditer(regex, data)
    first_regexs = re.finditer(first_regexs, data)
    first_match = first_regexs[0].group()
    
    os.wait()
    print(tmp)
    print(matches)
    tot = 0
    for match in matches:
        match = match.group()
        muls = re.findall(mul, match)
        print(muls)
        tot += len(muls)
    print("debug")
    print(tot)
#part1()
part2()