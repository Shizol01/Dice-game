import random

def user_input():
    while True:
        print("Enter dice format: xDy+z (e.g., 2D10+5, D6, 3D8-2)")
        dice = input("Your input: ").strip().upper()
        if dice:
            return dice
        print("Input cannot be empty. Try again.")

def input_validation():
    while True:
        dice = user_input()


        if "+" in dice:
            dice_part, modifier_part = dice.split("+")
            modifier = int(modifier_part)
        elif "-" in dice:
            dice_part, modifier_part = dice.split("-")
            modifier = -int(modifier_part)
        else:
            dice_part = dice
            modifier = 0


        if "D" not in dice_part:
            print("Invalid format. Try again.")
            continue

        parts = dice_part.split("D")
        if len(parts) != 2:
            print("Invalid format. Try again.")
            continue

        rolls, dice_type = parts
        rolls = int(rolls) if rolls.isdigit() else 1

        try:
            dice_type = int(dice_type)
        except ValueError:
            print("Invalid dice type. Try again.")
            continue

        return rolls, dice_type, modifier

def dice_validation(dice):
    available_dices = [3, 4, 6, 8, 10, 12, 20, 100]
    if dice not in available_dices:
        print("Invalid dice type. Try again.")
        return None
    return dice

def dice_game():
    while True:
        throw_numbers, dice, modificator = input_validation()
        dice_type = dice_validation(dice)

        if not dice_type:
            continue

        points = 0
        rolls_results = []

        for _ in range(throw_numbers):
            rnd = random.randint(1, dice_type)
            points += rnd
            rolls_results.append(rnd)

        points += modificator
        print(f"Rolls: {rolls_results} | Modifier: {modificator} | Total: {points}")

if __name__ == "__main__":
    dice_game()
