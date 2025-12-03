# https://adventofcode.com/
import logging

def parse(puzzle_input):
    return

def part1(data):
    return

def part2(data):
    return

if __name__ == "__main__":
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.DEBUG)
    
    day = 
    year = 2025
    
    puzzle_input = get_data(day=day, year=year)
    data = parse(puzzle_input)
    
    solution1 = part1(data)
    submit(solution1, part="a")
    
    solution2 = part2(data)
    submit(solution2, part="b")