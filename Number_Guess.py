import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose difficulty level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        max_num = 10
    elif choice == 2:
        max_num = 50
    elif choice == 3:
        max_num = 100
    else:
        print("Invalid choice! Defaulting to Medium level.")
        max_num = 50

    secret_number = random.randint(1, max_num)
    attempts = 0
    max_attempts = 10
    score = 100

    print(f"\nI have selected a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            score -= 10
            print("Too low! Try again.")
        elif guess > secret_number:
            score -= 10
            print("Too high! Try again.")
        else:
            print("\nCongratulations! You guessed the number.")
            print(f"Attempts used: {attempts}")
            print(f"Final Score: {score}")
            return

        print(f"Attempts left: {max_attempts - attempts}")

    print("\nGame Over!")
    print(f"The correct number was: {secret_number}")
    print(f"Final Score: {score}")

def main():
    while True:
        number_guessing_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

main()
