# https://adventofcode.com/
import logging
import numpy as np
import math

def parse(puzzle_input) -> np.array:
    points = np.array([[int(coordinate) for coordinate in line.split(",")] for line in puzzle_input.split("\n")])
    return points

def sort_into(clusters, pair):
    if all(pair[0]==pair[1]):
        return clusters
    match_0 = None
    match_1 = None
    for idx, c in enumerate(clusters):
        if np.any(np.all(pair[0]==c, axis=1)): # check if array is already within list of arrays
            match_0 = idx
        if np.any(np.all(pair[1]==c, axis=1)): # check if array is already within list of arrays
            match_1 = idx
    
    if all([match_0 is not None, match_1 is not None]):
        if match_0==match_1:
            # both already within the same cluster
            return clusters
        # merge existing clusters
        matches = [match_0, match_1]
        matches.sort()
        new_cluster = clusters.pop(matches[1])
        new_cluster += clusters.pop(matches[0])
        clusters += [new_cluster]
    elif not match_0 is None:
        # extend existing cluster 0
        clusters[match_0] += [pair[1]]
    elif not match_1 is None:
        # extend existing cluster 1
        clusters[match_1] += [pair[0]]
    else:
        # new cluster
        clusters += [[pair[0], pair[1]]]
    return clusters

def closest_pairs(a):
    n = len(a)
    
    # create empty array of nxn
    distances = np.full((n,n), np.inf)
    for x in range(0, n, 1):
        for y in range(0, x, 1):# only populate lower half of array with distances
            distances[x,y] = np.linalg.norm(a[x]-a[y])
    
    min_idxs = np.unravel_index(np.argsort(distances.ravel()), distances.shape)
    for i in range(0, n*n, 1):
        p1 = a[min_idxs[0][i]]
        p2 = a[min_idxs[1][i]]
        yield p1, p2

def part1(data):
    clusters = []
    pair = closest_pairs(data)
    
    for i in range(0, 1000, 1):
        p1, p2 = next(pair)
        logging.debug(f"{p1} <-> {p2}")
        clusters = sort_into(clusters, (p1, p2))
    
    cluster_lengths = [len(c) for c in clusters]
    cluster_lengths.sort(reverse=True)
    return math.prod(cluster_lengths[:3])

def part2(data):
    clusters = [[box] for box in data]
    pair = closest_pairs(data)
    
    while len(clusters)>1:
        p1, p2 = next(pair)
        logging.debug(f"{p1} <-> {p2}")
        clusters = sort_into(clusters, (p1, p2))
    
    result = p1[0]*p2[0]
    return result

if __name__ == "__main__":
    import timeit
    from aocd import get_data, submit
    #aocd-token at ~/.config/aocd/token
    
    logging.basicConfig(level=logging.INFO)
    
    day = 8
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