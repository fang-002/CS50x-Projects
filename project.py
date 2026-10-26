
def main():
    print("--- Welcome to My Expense Tracker ---")
    total = 0

    while True:
        print("\n1. Add Expense")
        print("2. Show Total")
        print("3. Exit")

        choice = input("Choose (1/2/3): ")

        if choice == "1":
            name = input("What did you buy? ")
            try:
                cost = float(input("How much did it cost? $"))
                total += cost
                print(f"Added {name} for ${cost}")
            except ValueError:
                print("Error: Please enter a valid number for the cost.")

        elif choice == "2":
            print(f"\nYour total expenses are: ${total}")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
