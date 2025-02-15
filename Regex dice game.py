import random
import re


DICE_REGEX = r"^(\d*)D(3|4|6|8|10|12|20|100)([+-]\d+)?$"


def user_input():
    """Pobiera i zwraca dane od użytkownika w formacie xDy+z"""
    while True:
        print("Enter dice format: xDy+z (e.g., 2D10+5, D6, 3D8-2)")
        dice = input("Your input: ").strip().upper()
        if dice:
            return dice
        print("Input cannot be empty. Try again.")


def parse_dice_input(dice):
    """Sprawdza poprawność formatu xDy+z i zwraca wartości"""
    match = re.match(DICE_REGEX, dice)

    if not match:
        print("Invalid format. Try again.")
        return None

    rolls, dice_type, modifier = match.groups()


    rolls = int(rolls) if rolls else 1


    dice_type = int(dice_type)
    modifier = int(modifier) if modifier else 0

    return rolls, dice_type, modifier


def roll_dice():
    """Obsługuje grę w kostki"""
    while True:
        dice = user_input()
        result = parse_dice_input(dice)

        if not result:
            continue

        throw_numbers, dice_type, modificator = result
        points = 0
        rolls_results = []

        for _ in range(throw_numbers):
            rnd = random.randint(1, dice_type)
            points += rnd
            rolls_results.append(rnd)

        points += modificator
        print(f"Rolls: {rolls_results} | Modifier: {modificator} | Total: {points}")


if __name__ == "__main__":
    roll_dice()
