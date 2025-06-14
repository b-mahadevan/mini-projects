# Python code for Secret_Code 

import random

from colorama import Fore, Style, init

init(autoreset=True)

def secret_number (digits):
    '''generate a random number with the given input digits'''

    code = ''

    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number)

    if number[9] == 0:
        number[9], number[8] = number[8], number[9]

    while digits:

            i = str(number.pop())
            code += i
            digits -= 1

    return code


def clue (guess_number, actual_number, digits):
    '''generate the glue by comparing guess and secret number'''

    clue = ''
    
    for i in range(digits):
          
        if guess_number[i] == actual_number[i]:
            clue += '\033[32mGreen \033[0m'

        elif guess_number[i] in actual_number:
            clue += '\033[33mYellow \033[0m'
        
        else:
            clue += '\033[31mRed \033[0m'

    return clue
                  

print("Hi, welcome to the Secret Code game.\n"
      "You will enter how many digits you want to solve in the secret code (between 3 and 6 digits).\n"
      "Once you enter, the secret code will be generated and the game begins.\n"
      "Just enter the number you have in mind.\n"
      "The clues are as follows:\n"
      "None of the number is repetative and number never start from zero\n"
      "\t'\033[32mGreen\033[0m' - The number is in the secret code and in the correct position\n"
      "\t'\033[33mYellow\033[0m' - The number is in the secret code but in the wrong position\n"
      "\t'\033[31mRed\033[0m' - The number is not in the secret code\n"
      "\nExample: If the code is '452' and the guess is '512', the clue will be 'Yellow Red Green'\n"
)
print(Style.BRIGHT + Fore.BLUE + "Are you ready? Let's get started!\n")
while True:
    while True:
        try:
            digits = int(input("How many digits do you want to decode? "))
            if digits < 3:
                print("Please enter a number greater than 2.")
            elif digits > 6:
                print("Please enter a number less than 7.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if digits == 3:
        max_attempts = 8

    elif digits == 4:
        max_attempts = 7

    elif digits == 5:
        max_attempts = 6

    else:
        max_attempts = 5    

    print(f"\nYou have {max_attempts} attempts to find the secret code.")

    secret_code = secret_number(digits)

    print(Style.BRIGHT + Fore.BLUE + "\nSuccesfully generated the secret code. Let's start.")

    while max_attempts:
        guess = input(f"\nEnter the {digits} digits number that is in your mind.\n")

        if len(guess) != digits or not guess.isdigit():
            print(f"Please, enter the {digits} digits number exactly.")
            print(Style.BRIGHT + Fore.BLUE + f"\nYou have {max_attempts} attempts remaining.")
            continue
        
        clues = clue(guess, secret_code, digits)
        print(f"{guess}: {clues}")

        if guess == secret_code:
            print(Style.BRIGHT + Fore.GREEN +f"\nCongrats you find the secret code. The secret code is {secret_code}.")
            break

        max_attempts -= 1
        print(Style.BRIGHT + Fore.RED + f"\n{max_attempts} attempts remaining")

    if guess != secret_code:
        print(Style.BRIGHT + f"\nSorry, try next game. The secret code is {secret_code}.")

    play_again = input("Do you want to play again? 'yes/no'\n")
    
    if play_again.strip().lower() in ['yes', 'y']:
        print("Thanks for your interest. Let we start.")
        continue

    elif play_again.strip().lower() in ['no', 'n']:
        print("Thanks, for playing.")
        break





    
     



