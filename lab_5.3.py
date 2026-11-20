import random
print("Welcome to Dice Simulator!")

while True:
    print("\n1. Roll the Dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        dice = random.randint(1, 6)
        print("You rolled:", dice)

    elif choice == '2':
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice. Please try again.")