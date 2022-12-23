"""Advent Of Code 2022 day 20."""
from tqdm import tqdm
import sys

file_name = sys.argv[1]
decryption_key = 811589153

with open(file_name, "r", encoding='utf-8') as fin:
    lines = fin.read().strip().split("\n")
    nums = list(map(int, lines))

    for i in range(len(nums)):
        nums[i] = (i, nums[i] * decryption_key)

n = len(nums)
og = nums.copy()


def swap(nums, a, b):
    """Swap elements in list."""
    assert (0 <= a < n) and (0 <= b < n)

    nums[a], nums[b] = nums[b], nums[a]
    return nums


for _ in tqdm(range(10)):
    for i, x in tqdm(og):
        for idx in range(n):
            if nums[idx][0] == i:
                break

        assert nums[idx][1] == x

        x %= (n - 1)

        if x > 0:
            current = idx
            for _ in range(x):
                nums = swap(nums, current, (current + 1) % n)
                current = (current + 1) % n

coords = [1000, 2000, 3000]

ans = 0
for zero_idx in range(n):
    if nums[zero_idx][1] == 0:
        break

for c in coords:
    ans += nums[(zero_idx + c) % n][1]

print(ans)
