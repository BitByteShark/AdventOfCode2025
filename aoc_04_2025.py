# https://adventofcode.com/
import logging
import numpy as np

def parse(puzzle_input):
    return np.array([[1 if col=="@" else 0 for col in row] for row in puzzle_input.split("\n")])

def surroundings(array, row, col):
    surroundings = []
    row_max, col_max = array.shape
    for r in range(row-1, row+2, 1):
        for c in range(col-1, col+2, 1):
            if (not 0<=c<col_max) or (not 0<=r<row_max) or (row == r and col == c):
                continue
            surroundings.append(array[r, c])
    return surroundings

def part1(data):
    counter = 0
    for r, row in enumerate(data):
        for c, col in enumerate(row):
            if col!=1:
                continue
            s = surroundings(data, r, c)
            if sum(s)<4:
                counter+=1
    return counter

def remove_rolls(array: np.array) -> np.array:
    row_max, col_max = array.shape
    for r in range(0, row_max, 1):
        for c in range(0, col_max, 1):
            if array[r, c]!=1:
                continue
            s = surroundings(array, r, c)
            if sum(s)<4:
                array[r, c] = 0
    return array

def part2(data):
    before = data
    changed = True
    while changed:
        after = remove_rolls(before.copy())
        changed = not np.array_equal(after, before)
        before = after
    return np.sum(data)-np.sum(after)

if __name__ == "__main__":
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.INFO)
    
    day = 4
    year = 2025
    
    puzzle_input = get_data(day=day, year=year)
    data = parse(puzzle_input)
    
    solution1 = part1(data)
    submit(solution1, part="a")
    
    solution2 = part2(data)
    submit(solution2, part="b")