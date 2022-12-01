"""Advent of the Code 2021.

Day 17 part 1
"""

# Imports
import datetime


# Get Data From File:
def get_data(filename):
    """Get data from file."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        _x, _y, x_area, y_area = data.split()
        x_area = x_area[2:-1]
        y_area = y_area[2:]

        x1, x2 = x_area.split('..')
        y1, y2 = y_area.split('..')

    return ((int(x1), int(x2)), (int(y1), int(y2)))


def iteritems(pos, vel):
    """Return New position and velocity.

    Args:
        pos (_type_): Position
        vel (_type_): Velocity
    return:
        pos (_type_): New position
        vel (_type_): New velocity
    """
    # Initialize new position and velocity
    new_pos = [0, 0]
    new_vel = [0, 0]

    # Calculate new position
    new_pos[0] = pos[0] + vel[0]
    new_pos[1] = pos[1] + vel[1]

    # Calculate new velocity
    # Vertical
    new_vel[1] = vel[1] - 1

    # Horizontal
    if vel[0] > 0:
        new_vel[0] = vel[0] - 1
    elif vel[0] < 0:
        new_vel[0] = vel[0] + 1

    # Return new position and velocity
    return new_pos, new_vel


def passed_target_area(pos, vel, target_area):
    """Check if Position Passed Target Area

    Params:
        pos (_type_): Position
        vel (_type_): Velocity
        target_area (_type_): Target Area

    Returns:
        _type_: True if passed target area, False if not
    """
    if pos[0] > target_area[0][1] and vel[0] > 0:
        return True
    if pos[0] < target_area[0][0] and vel[0] < 0:
        return True
    if pos[1] < target_area[1][0] and vel[1] < 0:
        return True

    return False


def is_within_target_area(pos, target_area):
    """Check if position is within target area.

    Params:
        pos (_type_): Position
        target_area (_type_): Target Area

    Returns:
        _type_: True if within target area, False if not
    """
    return target_area[0][0] <= pos[0] <= target_area[0][1]\
        and target_area[1][0] <= pos[1] <= target_area[1][1]


def meet_target_area(vel, target_area):
    """_summary_

        Args:
        pos (_type_): _description_
        target_area (_type_): _description_
    """
    pos = [0, 0]

    while not passed_target_area(pos, vel, target_area):
        if is_within_target_area(pos, target_area):
            return True
        else:
            new_pos, new_vel = iteritems(pos, vel)
            pos, vel = new_pos, new_vel
    return False


# Main Function:
def main():
    """Control flow of Script."""
    # Get Data Function
    target_area = get_data("day17.txt")
    print(f'Target Area: {target_area}')

    # Initialize Position and Velocity
    max_vel_y = abs(min(target_area[1]))
    yv = max_vel_y
    count = 0

    # Bruteforce velocity
    while yv >= target_area[1][0]:
        for xv in range(-400, 400):
            vel = [xv, yv]
            meet = meet_target_area(vel, target_area)
            if meet:
                count += 1
        yv -= 1
    print(f'Part 2: {count}')


if __name__ == '__main__':
    # Start Timer
    start_time = datetime.datetime.now()

    main()

    # End Timer
    end_time = datetime.datetime.now()
    print(f'Total Runtime: {end_time - start_time}')
    print('-' * 40)
