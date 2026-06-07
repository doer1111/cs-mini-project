def number_analyzer():
    print("\n--- Number Analyzer ---")

    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid number")
        return

    print("You entered:", number)

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

    print("Square:", number * number)
    print("---")
   

def calculator():
    print("\n--- Calculator ---")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")

    print("---")

def guessing_game():
    print("\n--- Guessing Game ---")
    print("I'm thinking of a number between 1 and 10...")

    import random
    secret = random.randint(1, 10)

    guess = None
    attempts = 0
    
    while guess != secret:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a number.")
            continue
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! You guessed it!")
            print("Attempts:", attempts)


while True:
    print("\n=== MAIN MENU ===")
    print("1. Number Analyzer")
    print("2. Calculator")
    print("3. Guessing Game")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        number_analyzer()

    elif choice == "2":
        calculator()
        
    elif choice == "3":
        guessing_game()
        
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")
