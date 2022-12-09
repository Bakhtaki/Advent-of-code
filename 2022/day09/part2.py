"""Advent of code 2022 day09 Solution"""
import sys



if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        lines = file.read().strip().splitlines()

    knots = [[0,0] for _ in range(10)]

    # touching fucntion
    def touching(x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1


    # move function
    def move(dx, dy):
        global knots
        knots[0][0] += dx
        knots[0][1] += dy

        for i in range(1, 10):
            hx, hy = knots[i-1]
            tx, ty = knots[i]

            if  not touching(hx, hy, tx, ty):
                sign_x = 0 if hx == tx  else (hx - tx) / abs(hx - tx)
                sign_y = 0 if hy == ty  else (hy - ty) / abs(hy - ty)

                tx += sign_x
                ty += sign_y

            knots[i] = [tx, ty]

    dd = { "R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1] }

    visited_tail = set()
    visited_tail.add(tuple(knots[-1]))

    for line in lines:
        operation, distance = line.split(" ")
        distance = int(distance)
        dx, dy = dd[operation]

        for _ in range(distance):
            move(dx, dy)
            visited_tail.add(tuple(knots[-1]))

    print("Part 2:", len(visited_tail))

