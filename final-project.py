import math

while True:

    print("\nSAVING PLANNER APP :)\n")

    # Step 1: Choose branch
    print("Type 1 to check if your goal is possible in a given time.")
    print("Type 2 to calculate how long it will take to reach your goal.")
    choice = input("Enter 1 or 2: ")

    while choice not in ["1", "2"]:
        print("Invalid input. Please enter 1 or 2.")
        choice = input("Enter 1 or 2: ")

    # Step 2: Ask for common inputs
    # Time unit selection
    time_unit = input("Choose your time unit (day/week/month/year): ").lower()
    while time_unit not in ["day", "week", "month", "year"]:
        print("Invalid input. Please type: day, week, month, or year.")
        time_unit = input("Choose your time unit (day/week/month/year): ").lower()

    # Conversion factor to days
    if time_unit == "day":
        factor = 1
    elif time_unit == "week":
        factor = 7
    elif time_unit == "month":
        factor = 30
    elif time_unit == "year":
        factor = 365

    # Input validation for common info
    goal = float(input("Enter (positive number) the amount of money (THB) you want to save: ")
                 .replace(",", "").replace(" ", ""))
    while goal <= 0:
        print("Goal must be a positive number.")
        goal = float(input("Enter (positive number) the amount of money (THB) you want to save: ")
                     .replace(",", "").replace(" ", ""))

    allowance = float(input(f"Enter your allowance (positive number) (THB per {time_unit}): ")
                      .replace(",", "").replace(" ", ""))
    while allowance <= 0:
        print("Allowance must be a positive number.")
        allowance = float(input(f"Enter your allowance (positive number) (THB per {time_unit}): ")
                          .replace(",", "").replace(" ", ""))

    expenses = float(input(f"Enter your expenses (positive number) (THB per {time_unit}): ")
                     .replace(",", "").replace(" ", ""))
    while expenses <= 0:
        print("Expenses must be a positive number.")
        expenses = float(input(f"Enter your expenses (positive number) (THB per {time_unit}): ")
                         .replace(",", "").replace(" ", ""))

    # Step 3: Branch 1: Check if goal is possible
    if choice == "1":
        time_value = float(input(f"Enter (positive number) the number of {time_unit}s you plan to save for: "))
        while time_value <= 0:
            print("Time must be a positive number.")
            time_value = float(input(f"Enter (positive number) the number of {time_unit}s you plan to save for: "))

        # Add "s" if plural
        if time_value != 1:
            time_label = time_unit + "s"
        else:
            time_label = time_unit

        # Convert to daily values
        allowance_per_day = allowance / factor
        expenses_per_day = expenses / factor
        daily_saving = allowance_per_day - expenses_per_day
        total_days = time_value * factor
        total_saving_possible = daily_saving * total_days
        required_daily = math.ceil(goal / total_days)

        print("\n--------------RESULT--------------")
        if daily_saving <= 0:
            print("Your expenses are higher than or equal to your allowance.")
            max_possible = allowance_per_day * total_days
            needed_cut = math.ceil((goal / total_days) + expenses_per_day - allowance_per_day)
            if max_possible >= goal:
                print(f"You need to cut at least {needed_cut} THB per day to reach your goal.")
            else:
                print("Even if you cut all your expenses, your goal is not possible.")
                print(f"The maximum you can save in {time_value} {time_label} is {math.floor(max_possible)} THB.")
                print(f"Your maximum daily saving would be {math.floor(allowance_per_day)} THB/day.")
        elif total_saving_possible >= goal:
            print("Your goal is possible to achieve!")
            print(f"You need to save at least {required_daily} THB per day to reach your goal.")
            print(f"If you save the maximum ({math.floor(daily_saving)} THB/day),")
            print(f"you'll have {math.floor(total_saving_possible)} THB saved after {time_value} {time_label}.")
        else:
            print("You can save some money daily but your goal is still too high.")
            print(f"The maximum you can save in {time_value} {time_label} is {math.floor(total_saving_possible)} THB.")
            print(f"Your maximum daily saving would be {math.floor(daily_saving)} THB/day.")

    # Step 4: Branch 2: Calculate time needed
    elif choice == "2":
        daily_saving = (allowance - expenses) / factor
        if daily_saving <= 0:
            print("Your daily saving is zero or negative. Goal cannot be reached.")
            needed_cut = math.ceil(expenses - allowance + 1)
            print(f"You need to cut at least {needed_cut} THB per {time_unit} to start saving.")
        else:
            interest_choice = input("Do you want to include interest? (yes/no): ").lower()
            if interest_choice == "yes":
                interest_rate = float(input("Enter annual interest rate (%, e.g., 3 for 3%): ")) / 100
                total_saved = 0
                total_days = 0
                while total_saved < goal:
                    total_saved += daily_saving
                    total_saved *= (1 + interest_rate / 365)
                    total_days += 1
            else:
                total_days = math.ceil(goal / daily_saving)

            # Convert total_days into user's chosen time_unit
            if time_unit == "day":
                time_needed = total_days
            elif time_unit == "week":
                time_needed = math.ceil(total_days / 7)
            elif time_unit == "month":
                time_needed = math.ceil(total_days / 30)
            elif time_unit == "year":
                time_needed = math.ceil(total_days / 365)

            # Add "s" if plural
            if time_needed != 1:
                time_label = time_unit + "s"
            else:
                time_label = time_unit

            print(f"\nIt will take approximately {time_needed} {time_label} to reach your goal.")

    restart = input("\nDo you want to restart the program (yes/no): ").lower()
    if restart != "yes":
        print("\nThank you for using the Saving Planner App! Byee :)")
        break