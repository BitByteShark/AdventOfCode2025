# https://adventofcode.com/
import logging
import numpy as np

def parse(puzzle_input):
    return puzzle_input.split("\n")

def part1(data):
    result_sum = 0
    for line in data:
        line = [int(digit) for digit in line]
        max_idx = np.argmax(line[:-1])
        first_digit = line[max_idx]
        second_digit = max(line[max_idx+1:])
        result_sum += 10*first_digit+second_digit
    return result_sum

def part2(data):
    result_sum = 0
    for line in data:
        line = [int(digit) for digit in line]
        
        digits = []
        digit_nr = 11
        while digit_nr>=1:
            max_idx = np.argmax(line[:-digit_nr]) # would not work for line[:-0]
            digits.append(line[max_idx])
            line = line[max_idx+1:] # only hand over the rest of the list
            digit_nr -= 1
        else:
            # case digit_nr == 0 (12th value)
            digits.append(max(line))
        
        result_sum += int("".join([str(d) for d in digits]))
    return result_sum

if __name__ == "__main__":
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.DEBUG)
    
    day = 3
    year = 2025
    
    puzzle_input = get_data(day=day, year=year)
    data = parse(puzzle_input)
    
    solution1 = part1(data)
    submit(solution1, part="a")
    
    solution2 = part2(data)
    submit(solution2, part="b")