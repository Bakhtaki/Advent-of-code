"""
This is scrip for advent of code 2021.

Level4 part1.
"""
import pprint as pp


def initiate_game():
    """We need to Simulate Start the Game."""
    with open('advent_of_code_l4.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    file.close()

    numbers = [int(number) for number in lines[0].split(',')]
    boards = []
    flags = []
    line_counter = 2

    while line_counter + 5 <= len(lines):
        boards.append([[int(cell) for cell in row.split()]
                       for row in lines[line_counter:line_counter + 5]])
        flags.append([[0 for cell in row.split()]
                      for row in lines[line_counter:line_counter + 5]])
        line_counter += 6
    return boards, numbers, flags


def start_game(i_boards, i_numbers, i_flags):
    """Will star a hand of game."""
    print(i_numbers)
    # pp.pprint(i_boards)
    # pp.pprint(i_flags)
    for each_number in numbers:
        called_number = each_number
        print(f'The number :{called_number} has been called.')
        i_flags, wining, board_idx = check_boards(called_number,
                                                  boards, i_flags)
        if wining:
            calculate_point(called_number, board_idx, i_flags)
            break


def check_boards(called_number, boards, i_flags):
    """This check called with boards."""
    # print(f'called number is : {called_number}')
    wining = False
    for board in range(len(boards)):
        for column in range(5):
            for row in range(5):
                if called_number == boards[board][column][row]:
                    # pp.pprint(f'number is exist in board {board}')
                    i_flags[board][column][row] = 1
                    # pp.pprint(i_flags)
                    wining = check_win(i_flags)
                    if wining:
                        print("******************************")
                        # pp.pprint([board])
                        return(i_flags, wining, board)
    return (i_flags, wining, board)


def check_win(array):
    for member in range(len(array)):
        for column in range(5):
            for row in range(5):
                if all(array[member][column]):
                    return True
    for member in range(len(array)):
        for column in range(5):
            for row in range(5):
                if all(array[member][row]):
                    return True
    return False


def calculate_point(number, board_idx, i_flags):
    """calculate Points for Winner."""
    print(f'Wining Number is : {number}')
    print(f'Winner board is :{board_idx}')
    # pp.pprint(i_flags[board_idx])
    # pp.pprint(boards[board_idx])
    unmarked_sum = 0
    for i in range(len(boards[board_idx])):
        for j in range(len(boards[board_idx])):
            if not i_flags[board_idx][i][j]:
                unmarked_sum += boards[board_idx][i][j]
    pp.pprint(f'Sum of Unmarked numbers is : {unmarked_sum}')
    pp.pprint(f'Your score is : {number * unmarked_sum}')


boards, numbers, flags = initiate_game()
start_game(boards, numbers, flags)
