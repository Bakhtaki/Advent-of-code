"""Advent of code 2022 day2 Solution."""


# Define Function to read input file
def read_input_file(input_file):
    """Read input file."""
    data = []
    # Read Data line by line
    with open(input_file, "r", encoding='utf-8') as file:
        for line in file:
            line_data = line.strip()
            data.append((line_data[0], line_data[2]))
    return data


# Define Function to check check_hand
def check_hand(p1, p2):
    """Check winner of Rock, paper, scissors."""
    # Player1: A: Rock, B: Paper, C: scissors
    # Player2: X: Rock, Y: Paper, Z: scissors
    score = 0
    # Check if player 2 wins
    if (p1 == "A" and p2 == "Y") or \
            (p1 == "B" and p2 == "Z") or (p1 == "C" and p2 == "X"):
        score += 6
    # Check if draw
    elif (p1 == "A" and p2 == "X") or \
            (p1 == "B" and p2 == "Y") or (p1 == "C" and p2 == "Z"):
        score += 3
    # Check if player 1 wins
    elif (p1 == "A" and p2 == "Z") or \
            (p1 == "B" and p2 == "X") or (p1 == "C" and p2 == "Y"):
        score += 0

    # Add score 1 for rock, 2 for paper, 3 for scissors
    if p2 == "X":
        score += 1
    elif p2 == "Y":
        score += 2
    elif p2 == "Z":
        score += 3

    return score


# Define Function To Solve Part 1
def part_1(data):
    """Solve part 1."""
    total_score = 0
    for oponent, player in data:
        total_score += check_hand(oponent, player)
    return total_score


# Define Choose choose_result
def choose_result(p_1, p_2):
    """Decryption of the result."""
    # Player1: A: Rock, B: Paper, C: scissors
    # Player2: X: Rock, Y: Paper, Z: scissors
    # Player2: X: Win, Y: Draw, Z: Lose
    score = 0
    choices_score = {"X": 1, "Y": 2, "Z": 3}

    # If P_2 is Z then P_1 need to wins
    if p_2 == "Z":
        score += 6
        # Select P_1 Choice to wins
        if p_1 == "A":
            p_2_choice = "Y"
            score += choices_score[p_2_choice]
        elif p_1 == "B":
            p_2_choice = "Z"
            score += choices_score[p_2_choice]
        elif p_1 == "C":
            p_2_choice = "X"
            score += choices_score[p_2_choice]

    # If P_2 is X then P_1 need to Lose
    if p_2 == "X":
        score += 0
        # Select P_1 Choice to Lose
        if p_1 == "A":
            p_2_choice = "Z"
            score += choices_score[p_2_choice]
        elif p_1 == "B":
            p_2_choice = "X"
            score += choices_score[p_2_choice]
        elif p_1 == "C":
            p_2_choice = "Y"
            score += choices_score[p_2_choice]

    # If P_2 is Y then P_1 need to draw
    if p_2 == "Y":
        score += 3
        # Select P_1 Choice to draw
        if p_1 == "A":
            p_2_choice = "X"
            score += choices_score[p_2_choice]
        elif p_1 == "B":
            p_2_choice = "Y"
            score += choices_score[p_2_choice]
        elif p_1 == "C":
            p_2_choice = "Z"
            score += choices_score[p_2_choice]

    return score


# Define function to solve part 2
def part_2(data):
    """Solve part 2."""
    total_score = 0
    for oponent, player in data:
        total_score += choose_result(oponent, player)
    return total_score


# Main Function
def main():
    """Main Function."""
    # Read input file
    data = read_input_file("input.txt")
    # Part 1
    part1 = part_1(data)
    print(f"part1: {part1}")
    # Part 2
    part2 = part_2(data)
    print(f"part2: {part2}")


if __name__ == "__main__":
    main()
