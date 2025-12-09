# https://adventofcode.com/
import logging
import numpy as np

def parse(puzzle_input):
    fresh_ranges, avail_ids = (section.split("\n") for section in puzzle_input.split("\n\n"))
    fresh_ranges = np.array([[int(value) for value in r.split("-")] for r in fresh_ranges])
    fresh_ranges = np.sort(fresh_ranges, 0)
    
    avail_ids = [int(value) for value in avail_ids]
    return fresh_ranges, avail_ids

def is_fresh(i, ranges):
    for start, end in ranges:
        if i<start:
            # all further ranges will start at higher value due to sort
            return False
        if start<=i<=end:
            return True
    return False

def part1(data):
    fresh_ranges, avail_ids = data
    count_fresh = 0
    for i in avail_ids:
        if is_fresh(i, fresh_ranges):
            count_fresh += 1
    return count_fresh

def collapse_ranges(original_ranges):
    reduced_ranges = []
    for original_range in original_ranges:
        og_r_start, og_r_end = original_range
        for red_idx, (red_r_start, red_r_end) in enumerate(reduced_ranges):
            if og_r_end < red_r_start or red_r_end < og_r_start:
                # current original range is completely outside of reduced range without contact
                # will check next range combination
                continue
            if og_r_start < red_r_start:
                # ranges are touching, og start is before reduced start -> reduced range will be extended
                logging.debug(f"Reduced: {red_r_start}-{red_r_end}, Original:{og_r_start}-{og_r_end} -> replace start")
                reduced_ranges[red_idx][0] = og_r_start
                break
            if red_r_end < og_r_end:
                # ranges are touching, og end is behind reduced end -> reduced will be extended
                logging.debug(f"Reduced: {red_r_start}-{red_r_end}, Original:{og_r_start}-{og_r_end} -> replace end")
                reduced_ranges[red_idx][1] = og_r_end
                break
            # og range has to be within reduced range
            logging.debug(f"Reduced: {red_r_start}-{red_r_end}, Original:{og_r_start}-{og_r_end} -> drop range")
            break
        else:
            # og range is separate and thus added as new reduced range
            logging.debug(f"Original:{og_r_start}-{og_r_end} -> added as separate range")
            reduced_ranges.append(original_range)
    reduced_ranges = np.array(reduced_ranges)
    return reduced_ranges

def part2(data):
    fresh_ranges, _ = data
    collapsed_ranges = np.array([])
    
    while True:
        collapsed_ranges = collapse_ranges(fresh_ranges)
        if np.array_equal(collapsed_ranges, fresh_ranges):
            break
        fresh_ranges = collapsed_ranges
    
    count_fresh = 0
    for start, end in collapsed_ranges:
        count_fresh += (end-start+1)
    return count_fresh

if __name__ == "__main__":
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.INFO)
    
    day = 5
    year = 2025
    
    puzzle_input = get_data(day=day, year=year)
    data = parse(puzzle_input)
    
    solution1 = part1(data)
    submit(solution1, part="a")
    
    solution2 = part2(data)
    submit(solution2, part="b")