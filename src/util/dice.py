import random

def roll(dice_num, dice_type):
    roll_total = 0

    for i in range(dice_num):
        roll = random.randint(1, int(dice_type))
        roll_total += roll

    return roll_total