import random

def dice_roll():

    roll = random.randint(1,6)
    return roll

print('Roll the dice!')

roll_the_dice = True

while roll_the_dice:

    choice = input('Roll the dice? Y/N: ').upper()
                          
    if choice == 'Y':
        number_rolled = dice_roll()
        print(f'You rolled {number_rolled}!')
    elif choice == 'N':
        roll_the_dice = False
    else:
        print('Please type Y or N: ')

print('Goodbye!')

input('Press Enter to exit...')
