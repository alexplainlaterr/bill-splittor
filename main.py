def split_bill():
    total_bill = float(input("Enter total bill amount: "))
    num_people = int(input("Enter number of people: "))

    spends = {}
    total_spent = 0
    for i in range(num_people):
        name = input(f"Enter name of person {i + 1}: ")
        amount_spent = float(input(f"Enter amount spent by {name}: "))
        spends[name] = amount_spent
        total_spent += amount_spent

    print("\nAmount each person should contribute:")
    for name, spent in spends.items():
        share = round((spent / total_spent) * total_bill, 2)
        print(f"{name} should contribute: ${share}")


if __name__ == "__main__":
    split_bill()
