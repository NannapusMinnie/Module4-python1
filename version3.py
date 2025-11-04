import math

print("SAVING PLANNER APP :)")

# Time unit selection (with up to 3 attempts)
attempts = 0
time_unit = ""

while attempts < 3:
    time_unit = input("Choose your time unit (days/weeks/months/years): ").lower()

    if time_unit == "days":
        break
    elif time_unit == "weeks":
        break
    elif time_unit == "months":
        break
    elif time_unit == "years":
        break
    else:
        attempts += 1
        print("Invalid input. Please type 'days', 'weeks', 'months', or 'years'.")
        print(f"You have {3 - attempts} attempts left.")

if attempts == 3:
    print("You entered an invalid unit 3 times. Program stopped.")
else:
    print(f"You selected '{time_unit}'.")


# Conversion factors to days
if time_unit == "days":
    factor = 1
elif time_unit == "weeks":
    factor = 7
elif time_unit == "months":
    factor = 30
elif time_unit == "years":
    factor = 365
else:
    print("Invalid time unit. Program stopped.")
    exit()

# basic inputs
goal = int(input("Enter (positive integer) the amount of money (THB) you want to save: "))
while goal <= 0:
    print("Goal must be a positive integer.")
    goal = int(input("Enter (positive integer) the amount of money (THB) you want to save: "))

allowance = int(input(f"Enter (positive integer) your allowance (THB) per {time_unit}: "))
while allowance <= 0:
    print("Allowance must be a positive integer.")
    allowance = int(input(f"Enter (positive integer) your allowance (THB) per {time_unit}: "))

expenses = int(input(f"Enter (positive integer) your expenses (THB) per {time_unit}: "))
while expenses <= 0:
    print("Expenses must be a positive integer.")
    expenses = int(input(f"Enter (positive integer) your expenses (THB) per {time_unit}: "))

# choice
print("\nType 1 to check if your goal is possible in a given time.")
print("Type 2 to calculate how long it will take to reach your goal.")
choice = input("Enter 1 or 2: ")

# Branch 1
if choice == "1":
    time_value = int(input(f"Enter the number of {time_unit} you plan to save for: "))
    while time_value <= 0:
        print("Time must be a positive integer.")
        time_value = int(input(f"Enter the number of {time_unit} you plan to save for: "))

    # Convert to daily values
    allowance_per_day = allowance / factor
    expenses_per_day = expenses / factor
    daily_saving = allowance_per_day - expenses_per_day
    total_days = time_value * factor
    total_possible = daily_saving * total_days
    required_daily = math.ceil(goal / total_days)

    print("\n=== RESULT ===")

    # Case A: expenses >= allowance
    if daily_saving <= 0:
        print("Your expenses are higher than or equal to your allowance.")

        max_possible = allowance_per_day * total_days  # max saving if expenses = 0
        needed_cut = math.ceil((goal / total_days) + expenses_per_day - allowance_per_day)

        if max_possible >= goal:
            print(f"You need to cut at least {needed_cut} THB per day to reach your goal.")
        else:
            print("Even if you cut all your expenses, your goal is not possible.")
            print(f"The maximum you can save in {time_value} {time_unit} is {math.floor(max_possible)} THB.")
            print(f"Your maximum daily saving would be {math.floor(allowance_per_day)} THB/day.")

    # Case B: goal is POSSIBLE
    elif total_possible >= goal:
        print("Your goal is possible to achieve!")
        print(f"You need to save at least {required_daily} THB per day to reach your goal.")
        print(f"If you save the maximum ({math.floor(daily_saving)} THB/day),")
        print(f"you'll have {math.floor(total_possible)} THB saved after {time_value} {time_unit}.")

    # Case C: goal too large
    else:
        print("Your goal is too large to achieve with your current allowance and expenses.")
        print(f"The maximum you can save in {time_value} {time_unit} is {math.floor(total_possible)} THB.")
        print(f"Your maximum daily saving would be {math.floor(daily_saving)} THB/day.")

# Branch 2
elif choice == "2":
    daily_saving = (allowance - expenses) / factor
    if daily_saving <= 0:
        print("Your daily saving is zero or negative. Goal cannot be reached.")
    else:
        # Ask about interest
        interest_choice = input("Do you want to include interest? (yes/no): ").lower()
        if interest_choice == "yes":
            interest_rate = float(input("Enter annual interest rate (in %, e.g., 3 for 3%): ")) / 100
            total_saved = 0
            total_days = 0
            while total_saved < goal:
                total_saved += daily_saving
                total_saved *= (1 + interest_rate / 365)  # daily compounding
                total_days += 1
        else:
            # No interest
            total_days = math.ceil(goal / daily_saving)

        # Convert total_days into user's chosen time_unit
        if time_unit == "days":
            time_needed = total_days
        elif time_unit == "weeks":
            time_needed = math.ceil(total_days / 7)
        elif time_unit == "months":
            time_needed = math.ceil(total_days / 30)
        elif time_unit == "years":
            time_needed = math.ceil(total_days / 365)

        print(f"\nIt will take approximately {time_needed} {time_unit} to reach your goal.")

# --- Invalid choice ---
else:
    print("Error: You didn't choose 1 or 2.")