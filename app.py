import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (Number between 1 and 50)")
    print("2. Medium (Number between 1 and 100)")
    print("3. Hard (Number between 1 and 200)")
    
    # Get difficulty level from the user
    difficulty = input("Enter difficulty (easy, medium, hard): ").lower()
    
    # Set the range based on difficulty level
    if difficulty == "easy":
        secret_number = random.randint(1, 50)
        print("You selected Easy mode. Guess the number between 1 and 50.")
    elif difficulty == "hard":
        secret_number = random.randint(1, 200)
        print("You selected Hard mode. Guess the number between 1 and 200.")
    else:
        secret_number = random.randint(1, 100)
        print("You selected Medium mode (default). Guess the number between 1 and 100.")

    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    number_guessing_game()
