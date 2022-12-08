"""Advent of code 2022 day 7 solution."""
import sys
from collections import defaultdict
from functools import lru_cache


filename = sys.argv[1]
with open(filename) as fin:
    blocks = ("\n" + fin.read().strip()).split("\n$ ")[1:]

path = []

dir_sizes = defaultdict(int)
children = defaultdict(list)


def parse(block):
    lines = block.split("\n")
    command = lines[0]
    outputs = lines[1:]

    parts = command.split(" ")
    op = parts[0]
    if op == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])

        return

    abspath = "/".join(path)
    assert op == "ls"

    sizes = []
    for line in outputs:
        if not line.startswith("dir"):
            sizes.append(int(line.split(" ")[0]))
        else:
            dir_name = line.split(" ")[1]
            children[abspath].append(f"{abspath}/{dir_name}")

    dir_sizes[abspath] = sum(sizes)


for block in blocks:
    parse(block)


# Do DFS
@lru_cache(None)  # Cache may not be strictly necessary
def dfs(abspath):
    size = dir_sizes[abspath]
    for child in children[abspath]:
        size += dfs(child)
    return size


ans = 0
for abspath in dir_sizes:
    if dfs(abspath) <= 100000:
        ans += dfs(abspath)

print(ans)
