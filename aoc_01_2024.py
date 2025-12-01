# https://adventofcode.com/
import logging

def parse(puzzle_input):
    for instruction in puzzle_input.split("\n"):
        sign = 1 if instruction[0]=="R" else -1
        yield sign*int(instruction[1:])

def part1(data):
    instructions = list(data)
    position = 50
    password = 0
    for instruction in instructions:
        position += instruction
        if position%100==0:
            password += 1
    return password

def part2(data):
    instructions = list(data)
    position = 50
    password = 0
    for instruction in instructions:
        if instruction >= 0:
            partial_rotation = instruction%100
            full_rotations = int((instruction-partial_rotation)/100)
            if partial_rotation >= (100-position) and position != 0:
                password += 1
        else:
            partial_rotation = instruction%-100
            full_rotations = int((instruction-partial_rotation)/-100)
            if abs(partial_rotation) >= position and position != 0:
                password += 1
        
        password += full_rotations
        position = (position+partial_rotation)%100
    return password

if __name__ == "__main__":
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.DEBUG)
    
    day = 1
    year = 2025
    
    puzzle_input = get_data(day=day, year=year)
    
    solution1 = part1(parse(puzzle_input))
    submit(solution1, part="a")
    
    solution2 = part2(parse(puzzle_input))
    submit(solution2, part="b")