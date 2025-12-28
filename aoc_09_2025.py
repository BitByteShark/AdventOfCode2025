# https://adventofcode.com/
import logging
import numpy as np

def parse(puzzle_input):
    return [np.array([int(number) for number in line.split(",")]) for line in puzzle_input.split("\n")]

def part1(data):
    max_area = 0
    n = len(data)
    pairings = np.full((n,n), np.nan)
    for i in range(0, n, 1):
        for j in range(0, i, 1):# only populate lower half of array
            x_distance = 1+abs(data[i][0]-data[j][0])
            y_distance = 1+abs(data[i][1]-data[j][1])
            area = x_distance*y_distance
            pairings[i,j] = area
            if area>max_area:
                max_area = area
    return max_area

def part2(data):
    return

if __name__ == "__main__":
    import timeit
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.DEBUG)
    
    day = 9
    year = 2025
    
    puzzle_input = get_data(day=day, year=year)
    
    t1 = timeit.default_timer()
    solution1 = part1(parse(puzzle_input))
    t2 = timeit.default_timer()
    logging.info(f"Solving P1 took: {t2-t1} sec")
    submit(solution1, part="a")
    
    t3 = timeit.default_timer()
    solution2 = part2(parse(puzzle_input))
    t4 = timeit.default_timer()
    logging.info(f"Solving P2 took: {t4-t3} sec")
    submit(solution2, part="b")