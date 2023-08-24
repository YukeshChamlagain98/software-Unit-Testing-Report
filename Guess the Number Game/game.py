"""
Guess the Number Game

This module implements a simple number guessing game where the player
tries to guess a randomly generated 4-digit number.

Author: Yukesh Chamlagain
Date: 23/08/2023
"""
import random


def generate_random_number():
    """Generate a random 4-digit number."""
    return random.randint(1000, 9999)


def evaluate_guess(target, guess):
    """Evaluate the player's guess and provide hints."""
    target_str = str(target)
    guess_str = str(guess)
    result = ''

    for i in range(4):
        if guess_str[i] == target_str[i]:
            result += 'O'
        elif guess_str[i] in target_str:
            result += 'X'

    return result


def play_game():
    """Play the game."""
    target_number = generate_random_number()
    attempts = 0
    max_attempts = 10  # Set your desired maximum number of attempts here

    while attempts < max_attempts:
        try:
            player_guess = int(input("Enter your guess (4-digit number): "))
            if not 1000 <= player_guess <= 9999:
                print("Please enter a valid 4-digit number.")
                continue

            attempts += 1

            if player_guess == target_number:
                print(f"Congratulations! You guessed the number "
                      f"{target_number} in {attempts} attempts.")
                break
            hint = evaluate_guess(target_number, player_guess)
            print("Hint:", hint)

        except ValueError:
            print("Please enter a valid numeric input.")

    else:
        print(f"Sorry, you've reached the maximum number of attempts. "
              f"The correct number was {target_number}.")


if __name__ == "__main__":
    play_game()
