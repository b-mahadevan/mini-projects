# Python code for Secret_Code 

import random

def secret_number (digits):
    '''generate a random number with the given input digits'''

    code = ''

    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(number)
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
      "None of the number is repetative and number never start from zero"
      "\t'\033[32mGreen\033[0m' - The number is in the secret code and in the correct position\n"
      "\t'\033[33mYellow\033[0m' - The number is in the secret code but in the wrong position\n"
      "\t'\033[31mRed\033[0m' - The number is not in the secret code\n"
      "Example: If the code is '452' and the guess is '512', the clue will be 'Yellow Red Green'\n"
      "Are you ready? Let's get started!"
)
while True:
    digits = int(input("How many digits do you want to decode?"))

    while True:
        if digits<3:
            print("Please, enter the digits greater than 2.")
            digits = int(input("How many digits do you want to decode?"))

        elif digits>7:
            print("Please, enter the digits less than 8.")
            digits = int(input("How many digits do you want to decode?"))
    
        else:
            break

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

    print("\nSuccesfully generated the secret code. Let's start.")


    while max_attempts:
        guess = input(f"Enter the {digits} digits number that is in your mind.")

        if len(guess) != digits or not guess.isdigit():
            print(f"Please, enter the {digits} digits number exactly.")
            print(f"You have {max_attempts} attempts remaining.")
            continue
        
        clues = clue(guess, secret_code, digits)
        print(f"{guess}: {clues}")

        if guess == secret_code:
            print(f"\nCongrats you find the secret code. The secret code is {secret_code}.")
            break

        max_attempts -= 1
        print(f"{max_attempts} attempts remaining")

    if guess != secret_code:
        print(f"\nSorry, try next game. The secret code is {secret_code}.")

    play_again = input("Do you want to play again? 'yes/no'")
    
    if play_again.lower() == 'yes':
        print("Thanks for your interest. Let we start.")
        continue

    elif play_again.lower() == 'no':
        print("Thanks, for playing.")
        break





    
     



