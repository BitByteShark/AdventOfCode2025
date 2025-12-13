# https://adventofcode.com/
import logging
import numpy as np
import math

def parse(puzzle_input):
    raw_lines = puzzle_input.split("\n")
    seperator_locations = []
    prev_char = None
    for idx, char in enumerate(raw_lines[-1]):
        if char!=" " and prev_char==" ":
            seperator_locations += [idx-1]
        prev_char = char
    
    lines = []
    for line in raw_lines:
        line = list(line)
        for idx, char in enumerate(line):
            if idx in seperator_locations:
                line[idx] = ","
            elif char == " ":
                line[idx] = ""
        lines += [line]
    
    return lines

def evaluate(line, operator):
    if operator == "+":
        return sum(line)
    elif operator == "*":
        return math.prod(line)
    else:
        raise Exception(f"{operator} is no valid operator")

def part1(data):
    lines = ["".join(line).split(",") for line in data]
    problems = np.rot90(np.array([[int(value) for value in line] for line in lines[:-1]]))
    operators = list(reversed(lines[-1]))
    
    grand_total = 0
    for idx, line in enumerate(problems):
        operator = operators[idx]
        grand_total += evaluate(line, operator)
    return int(grand_total)

def part2(data):
    operators = list(reversed([op for op in data[-1] if op not in (",", "")]))
    problems = np.rot90(np.array(data[:-1]))
    
    grand_total = 0
    idx = 0
    group = []
    for line in problems:
        if line[0]==",":
            operator = operators[idx]
            grand_total += evaluate(group, operator)
            group = []
            idx += 1
        else:
            group += [int("".join(line))]
    
    grand_total += evaluate(group, operators[-1])
    return grand_total

if __name__ == "__main__":
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.DEBUG)
    
    day = 6
    year = 2025
    
    puzzle_input = get_data(day=day, year=year)
    data = parse(puzzle_input)
    
    solution1 = part1(data)
    submit(solution1, part="a")
    
    solution2 = part2(data)
    submit(solution2, part="b")