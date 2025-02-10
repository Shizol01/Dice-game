import random
from curses.ascii import isdigit


def user_input():
    while True:
        try:
            print("y – type of dice to use (e.g. D6, D10),\n"
                  "x – number of dice rolls; if we throw once, this parameter is negligible,\n"
                  "z – number to be added (or subtracted) to the roll result (optional).")
            dice = input("Please enter your dice in format xDy+z: ")
            return dice
        except ValueError:
            print("You didn't enter a valid number. Try again.")

def input_validation():
    while True:
        dice = user_input()
        try:
            div1, div2 = dice.split("D")
            div2, div3 = div2.split("+")
        except ValueError:
            print("You didn't enter a valid number. Try again.")
            continue
        try:
            div1, div2, div3 = int(div1), int(div2), int(div3)
        except ValueError:
            print("You didn't enter a valid parameters")
            continue
        return div1, div2, div3


def dice_validation(dice):
    while True:
        avalaible_dices = [3, 4, 6, 8, 10, 12, 20, 100]
        if dice not in avalaible_dices:
            print("You didn't enter a valid number of dice points. Try again.")
            continue
        else:
            return dice

def dice_game():
        throw_numbers, dice, modificators = input_validation()
        dice_type = dice_validation(dice)
        points = 0 + modificators
        for _ in range(throw_numbers):
            rnd = random.randint(1, dice_type)
            points += rnd
            print(rnd, points)
        print(f"You rolled {points} points.")




if __name__ == "__main__":
   dice_game()