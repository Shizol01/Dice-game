import random
from curses.ascii import isdigit


def user_input():
    '''
    Asks the user to input a die roll command in the format xDy+z.

    :rtype string:
    :return:User input as a string.
    '''
    while True:
        try:
            print("y – type of dice to use (e.g. D6, D10),\n"
                  "x – number of dice rolls min. value 1 ,\n"
                  "z – number to be added (or subtracted) to the roll result (optional).")
            dice = input("Please enter your dice in format xDy+z: ")
            return dice
        except ValueError:
            print("You didn't enter a valid number. Try again.")

def input_validation():
    '''
    Validates and parses the user input to extract roll count, dice type, and modifier

    :rtype int:
    :return: roll count, dice type, and modifier
    '''
    while True:
        dice = user_input()
        try:
            div1, div2 = dice.split("D")
            if "+" in div2:
                div2, div3 = div2.split("+")
                div3 = int(div3)
            elif "-" in div2:
                div2, div3 = div2.split("-")
                div3 = -int(div3)
            else:
                div3 = 0
            div1 = int(div1) if div1 else 1
            div2 = int(div2)

        except ValueError:
            print("Please enter your dice in format xDy+z:")
            continue

        return div1, div2, div3


def dice_validation(dice):
    '''
    Validates dice type
    :param dice:
    :rtype int:
    :return: dice if correct type
    '''
    while True:
        available_dices = [3, 4, 6, 8, 10, 12, 20, 100]
        if dice not in available_dices:
            print("You didn't enter a valid number of dice points. Try again.")
            continue
        else:
            return dice

def dice_game():
    '''
    Main game function

    :rtype string:
    :return: Information how much points rolled
    '''
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