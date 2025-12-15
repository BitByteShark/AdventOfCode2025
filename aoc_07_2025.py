# https://adventofcode.com/
import logging
import numpy as np

def parse(puzzle_input):
    lines = puzzle_input.split("\n")
    starting_point = None
    for row_idx, row in enumerate(lines):
        for col_idx, col in enumerate(row):
            if col == "S":
                starting_point = (row_idx, col_idx)
                break
        if starting_point:
            break
    return np.array([list(line) for line in lines]), starting_point

def solve(data):
    canvas, starting_point = data
    split_locations = {}
    
    def track_beam(row_idx, col_idx, canvas):
        """
        track beam to next split or edge of canvas
        return number of sparate downstream beams
        """
        nonlocal split_locations
        path = canvas[row_idx+1:, col_idx]
        
        for row_in_path, pixel in enumerate(path):
            current_location = (row_idx+row_in_path+1, col_idx)
            if pixel=="^":
                return split(current_location[0], current_location[1], canvas)
        return 1
    
    def split(row_idx, col_idx, canvas) -> int:
        """
        split beam at location and track sum of downstream beams
        """
        nonlocal split_locations
        if (row_idx, col_idx) in split_locations.keys():
            return split_locations[(row_idx, col_idx)]
        
        logging.debug(f"start of: {(row_idx, col_idx)}")
        right_downstream_splits = track_beam(row_idx, col_idx+1, canvas)
        left_downstream_splits = track_beam(row_idx, col_idx-1, canvas)
        
        downstream_splits = right_downstream_splits+left_downstream_splits
        
        split_locations.update({(row_idx, col_idx): downstream_splits})
        logging.debug(f"end of: {(row_idx, col_idx)} -> {downstream_splits}")
        return downstream_splits
    
    particle_arrivals = track_beam(starting_point[0], starting_point[1], canvas)
    return split_locations, particle_arrivals

def part1(data):
    splits, _ = solve(data)
    split_count = len(splits.keys())
    return split_count

def part2(data):
    _, particle_arrivals = solve(data)
    return particle_arrivals

if __name__ == "__main__":
    import timeit
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.INFO)
    
    day = 7
    year = 2025
    
    test_data = \
""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    puzzle_input = parse(test_data)
    test_result = part1(puzzle_input) # 21
    test_result2 = part2(puzzle_input) # 40
    
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