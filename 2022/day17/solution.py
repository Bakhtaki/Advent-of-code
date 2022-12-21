"""Advent of Code 2022 DAY17 solution."""

import sys


# CLASS GAME
class Game:
    """Create Tetris Game Objects."""
    def __init__(self, stream) -> None:
        """Init Game Object."""
        self.stream = stream
        self.rock_number = 0
        self.stream_id = 0
        self.left_wall = 0
        self.right_wall = 0
        self.height = 0
        self.grid = set()
        for i in range(0, 9):
            self.grid.add((i, 0))
        self.new_rock()
        self.signatures = {}

    # Define Function to Drop Rock from Top.
    def drop_rock(self) -> None:
        """Drop Rock from Top."""
        while True:
            # Push stream
            self.push(self.stream[self.stream_id] == '<')
            if self.fall():
                break
        sig = self.signature()
        hit = None, None

        if sig in self.signatures:
            hit = self.signatures[sig] -\
                self.signatures[sig[0],
                                self.rock_number - self.signatures[sig][1]]
        self.signatures[sig] = (self.height, self.rock_number)
        return hit

    # Define Push Function
    def push(self, left=True):
        dx = -1 if left else 1
        if all(0 < x + dx < 8 for x, y in self.rock) and all((x + dx, y) not in self.grid for x, y in self.rock):
            self.rock = set((x + dx, y) for x, y in self.rock)
        self.stream_id = (self.stream_id + 1) % len(self.stream)

    # Define Fall Function
    def fall(self):
        if all((x, y + 1) not in self.grid for x, y in self.rock):
            self.rock = set((x, y + 1) for x, y in self.rock)
            return False
        self.height = max(y for x, y in self.rock) + self.height

        for x, y in self.rock:
            self.grid.add((x, y))
        self.new_rock()
        return True

    # Define Print Function
    def print(self):
        top = max[self.height] + [y for x, y in self.rock] + 2
        for r in range(top, -1, -1):
            print(f'{r:5}|', end='')
            for c in range(1, 8):
                if (c, r) in self.grid:
                    print('#', end='')
                elif (c, r) in self.rock:
                    print('@', end='')
                else:
                    print(' ', end='')
            print('|')

    # Define Signature Function
    def signature(self):
        rows = 40
        points = set(self.rock_number % 5)
        for y in range(rows):
            for x in range(1, 8):
                if (x, y + self.height - rows) in self.grid:
                    points.add((x, y))
        return frozenset(points)

    def new_rock(self) -> None:
        """Create a New Rock"""
        self.rock = set()
        num = self.rock_number % 5

        if num == 0:
            for x in range(3, 7):
                self.rock.add((x, self.height + 4))
        elif num == 1:
            self.rock.add((3, self.height + 5))
            self.rock.add((4, self.height + 4))
            self.rock.add((4, self.height + 5))
            self.rock.add((4, self.height + 6))
            self.rock.add((5, self.height + 5))
        elif num == 2:
            for x in range(3, 6):
                self.rock.add((x, self.height + 4))
            for y in range(5, 7):
                self.rock.add((5, self.height + y))
        elif num == 3:
            for y in range(4, 8):
                self.rock.add((3, self.height + y))
        elif num == 4:
            for x in range(3, 5):
                for y in range(4, 6):
                    self.rock.add((x, self.height + y))
        else:
            assert False
        self.rock_number += 1


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r', encoding="utf-8") as f:
        line = f.read().strip()

    game = Game(line)
    numbers_to_drop = int(sys.argv[2]) if len(sys.argv) > 2 else 2022
    for i in range(numbers_to_drop):
        game.drop_rock()

    # Par One hight
    print('Part One:', game.height)
