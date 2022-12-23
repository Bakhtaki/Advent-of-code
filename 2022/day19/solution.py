"""Advent of code 2022 day 19 puzzle solution."""

# Imports
import sys
import re
import math
import pprint as pp
from collections import deque


# Define functions to solve the puzzle
def solve(blue_print, t):
    """Solve the puzzle."""
    # Each ore robot costs 4 ore
    # Each clay robot costs 4 ore
    # Each obsidian robot costs 3 ore and 7 clay
    # Each Geode robot costs 2 ore and 11 obsidian

    # Create raw materials
    row_costs = list(map(int, re.findall(r"\d+", blue_print)))
    costs = (
        (row_costs[1], 0, 0, 0),
        (row_costs[2], 0, 0, 0),
        (row_costs[3], row_costs[4], 0, 0),
        (row_costs[5], 0, row_costs[6], 0),
    )

    # State of the factory:
    # (time,
    # resources(ore, clay, obsidian, geode)),
    # (robots(ore, clay, obsidian, geode)),

    queue = deque()
    queue.append((t, (0, 0, 0, 0), (1, 0, 0, 0)))

    visited = set()
    optimal = 0
    max_robots = [max(costs[i] for costs in costs) for i in range(4)]

    while queue:
        t, stuff, robots = queue.popleft()

        # Minimum Geode robots
        min_geode = stuff[3] + t * robots[3]
        # Compute the min_geode with optimal robots
        if min_geode > optimal:
            optimal = min_geode
        if (t, stuff, robots) in visited:
            continue
        visited.add((t, stuff, robots))
        if t == 0:
            continue

        # Produce the optimal amount of Geode
        for resource in range(4):
            # Check Max Needed Materials
            if resource != 3 and robots[resource] > max_robots[resource]:
                continue
            # Check if we have enough robots
            if any(
                robots[rid] == 0 for rid,
                cost in enumerate(costs[resource]) if cost > 0
            ):
                continue
            # Wait to Have Enough Materials to Produce robots
            wait = max(
                [
                    math.ceil((cost - stuff[rid]) / robots[rid])
                    for rid, cost in enumerate(costs[resource]) if cost
                ]
                + [0]
            )

            if t - wait - 1 <= 0:
                continue
            # New Stuff
            next_stuff = [
                stuff[i] +
                (robots[i] * wait + 1) - costs[resource][i] for i in range(4)
            ]

            # New Robots
            next_robots = list(robots)
            next_robots[resource] += 1

            for i in range(3):
                next_stuff[i] = min(next_stuff[i],
                                    max_robots[i] * (t - wait - 1))

            queue.append((t - wait - 1, tuple(next_stuff), tuple(next_robots)))

    return optimal


if __name__ == "__main__":
    # Read input
    file_name = sys.argv[1]
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()

    pp.pprint(lines)

    part1 = 0
    # Part 1.
    for i, line in enumerate(lines):
        part1 += (i + 1) * solve(line, 24)
    print(f"Part 1: {part1}")

    # Part 2.
    part2 = 1
    for line in lines[:3]:
        part2 *= solve(line, 32)
    print(f"Part 2: {part2}")
