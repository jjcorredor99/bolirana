import random

# Define points for each input
INPUT_POINTS = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60,
    7: 70,
    8: 80,
    9: 90,
    10: 100  # Input 10 is the bonus-triggering input
}

def calculate_score(input_id):
    """
    Calculate the score for a given input.

    Args:
        input_id (int): The ID of the input triggered.

    Returns:
        int: The score for the input, including any bonuses.
    """
    if input_id not in INPUT_POINTS:
        raise ValueError(f"Invalid input ID: {input_id}")

    # Regular points
    score = INPUT_POINTS[input_id]

    # Apply bonus if input is 10
    if input_id == 10:
        bonus = random.randint(250, 1000)
        print(f"🎉 Bonus triggered! Bonus points: {bonus}")
        score += bonus

    return score
