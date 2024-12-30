import random


def guess_the_number():
    secret_number = random.randint(1, 100)

    print("I have picked a number between 1 and 100. Can you guess it?")

    attempts = 0

    while True:
        player_guess = int(input("Enter your guess: "))

        attempts += 1

        if player_guess < secret_number: 
            print("Your guess is too low. Try again!")
        elif player_guess > secret_number:
            print("Your guess is too high. Try again!")
        else:
            print(
                f"Congratulations! You guessed the number {secret_number} in {attempts} tries."
            )
            break


guess_the_number()
