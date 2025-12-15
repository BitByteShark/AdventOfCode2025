# https://adventofcode.com/
import logging

def parse(puzzle_input):
    return

def part1(data):
    return

def part2(data):
    return

if __name__ == "__main__":
    import timeit
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.DEBUG)
    
    day = 
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