"""Advent of code 2022 day 12 solution."""
import sys
import pprint as pp
from string import ascii_lowercase
from heapq import heappush, heappop


# Find the shortest path between Start and End using Dijkstra's algorithm
def dijkstra(grid: list, start: tuple, end: tuple) -> None:
    """Find the shortest path  using Dijkstra's algorithm."""
    n = len(grid)
    m = len(grid[0])

    visited = [[False] * m for _ in range(n)]
    heap = [(0, start[0], start[1])]

    while True:
        step, i, j = heappop(heap)

        # if in visited
        if visited[i][j]:
            continue
        visited[i][j] = True

        if (i, j) == end:
            return step

        for ii, jj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            di = i + ii
            dj = j + jj

            # if out of bounds
            if di < 0 or di >= n or dj < 0 or dj >= m:
                continue
            # if neighbors values more than current
            if grid[di][dj] > grid[i][j] + 1:
                continue
            # add to heap
            heappush(heap, (step + 1, di, dj))


if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding='utf-8') as file:
        data = file.read().strip()

    # Create list of lists from data
    data = [list(line) for line in data.splitlines()]

    # length of the data and length of the first line
    length = len(data)
    width = len(data[0])

    mapped_data = [[0 for _ in range(width)] for _ in range(length)]
    for i in range(length):
        for j in range(width):
            if data[i][j] == 'S':
                start = (i, j)
                mapped_data[i][j] = 0
            elif data[i][j] == 'E':
                end = (i, j)
                mapped_data[i][j] = 25
            elif data[i][j] in ascii_lowercase:
                mapped_data[i][j] = ord(data[i][j]) - 97
    # Part 1
    print("Part 1")
    answer1 = dijkstra(mapped_data, start, end)
    print(f"Answer: {answer1}")

    # Part 2
    print("Part 2")
    answer2 = sys.maxsize
    candidates = []

    # Find all 0 values in the grid
    for i in range(length):
        for j in range(width):
            if mapped_data[i][j] == 0:
                candidates.append((i, j))

    # Find the shortest path between each 0 and the End
    for candidate in candidates:
        answer2 = min(answer2, dijkstra(mapped_data, candidate, end))

    print(f"Answer: {answer2}")

