import random


def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| • |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|•  |",
            "|   |",
            "|  •|",
            "-----",
        ),
        3: (
            "-----",
            "|•  |",
            "| • |",
            "|  •|",
            "-----",
        ),
        4: (
            "-----",
            "|• •|",
            "|   |",
            "|• •|",
            "-----",
        ),
        5: (
            "-----",
            "|• •|",
            "| • |",
            "|• •|",
            "-----",
        ),
        6: (
            "-----",
            "|• •|",
            "|• •|",
            "|• •|",
            "-----",
        ),

    }
    roll = input("Roll the dice? (Yes/No):")

    while roll.lower() == "YES".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rooled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("Roll again? (Yes/No)")


roll_dice()
