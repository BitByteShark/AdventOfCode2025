# https://adventofcode.com/
import logging
import re
from typing import List

def parse(puzzle_input):
    for line in re.split(",", puzzle_input):
        yield line

def is_silly_pattern_p1(value: int) -> bool:
    value = str(value)
    length = len(value)
    if length%2 != 0:
        return False
    
    mid = int(length/2)
    if value[:mid] != value[mid:]:
        return False
    return True

def get_split_sections(phrase: str, split_count: int) -> List[str]:
    phrase_length = len(phrase)
    section_length = int(phrase_length/split_count)
    for i in range(0, split_count, 1):
        section_start = i*section_length
        section_end = section_start+section_length
        yield phrase[section_start:section_end]

def is_silly_pattern_p2(value: int) -> bool:
    value_text = str(value)
    length = len(value_text)
    divisors = range(2, length+1, 1) # primes would be more efficient and possible here?
    for divisor in divisors:
        if length%divisor==0 and len(set(get_split_sections(value_text, divisor)))==1:
            return True
    return False

def part(data, part_nr):
    invalid_sum = 0
    for line in data:
        start, end = line.split("-")
        for value in range(int(start), int(end)+1, 1):
            if (part_nr == 1 and is_silly_pattern_p1(value)) or (part_nr == 2 and is_silly_pattern_p2(value)):
                invalid_sum += value
    return invalid_sum

if __name__ == "__main__":
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.DEBUG)
    day = 2
    year = 2025

    puzzle_input = get_data(day=day, year=year)

    solution1 = part(parse(puzzle_input), 1)
    submit(solution1, part="a")

    solution2 = part(parse(puzzle_input), 2)
    submit(solution2, part="b")