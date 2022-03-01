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


# Main Function:
def main():
    """Control flow of Script."""
    # Get Data Function
    target_area = get_data("day17_test.txt")
    print(f'Target Area: {target_area}')

    max_height = 0

    for xv in range(-100, 100):
        for yv in range(abs(target_area[1][0])):
            vel = (xv, yv)
            pos = (0, 0)
            flag = True
            while flag:
                new_pos, new_vel = iteritems(pos, vel)
                print(f'New Position: {new_pos}, New Velocity: {new_vel}')
                max_height = max(max_height, new_pos[1])
                if new_pos[1] + new_vel[1] < target_area[1][0]:
                    flag = False
                    break
                pos = new_pos
                vel = new_vel

    print(f'Max Height: {max_height}')


if __name__ == '__main__':
    # Start Timer
    start_time = datetime.datetime.now()

    main()

    # End Timer
    end_time = datetime.datetime.now()
    print(f'Total Runtime: {end_time - start_time}')
