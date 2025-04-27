import random
while True:
    choice = input("Do you want to roll the dice? (y/n): ").lower()
    if choice == "y":
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f"({num1}, {num2})")
    elif choice == "n":
        print("Thank you for playing!!!")
        break
    else:
        print("Invalid choice")
