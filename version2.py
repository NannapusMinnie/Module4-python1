import math

print("SAVING PLANNER APP :)")
print("Type 1 to check if your save up goal is possible in a given time")
print("Type 2 to calculate days needed to reach a goal")

choice = input("Enter 1 or 2: ")


if choice == "1":
    # Ask for Goal
    goal = int(input("Enter (in positive integer) amount of money (THB) you want to save: "))
    while goal <= 0:
        print("Goal can't be negative or zero.")
        goal = int(input("Please enter a valid positive amount: "))

    # Ask for time unit
    time_unit = input("Enter time unit (days/weeks/months/years): ").lower()
    time_value = int(input(f"Enter number of {time_unit}: "))
    while time_value <= 0:
        print("Time must be a positive number.")
        time_value = int(input(f"Enter number of {time_unit}: "))

    # Convert to days for calculation
    if time_unit == "days":
        time_limit = time_value
    elif time_unit == "weeks":
        time_limit = time_value * 7
    elif time_unit == "months":
        time_limit = time_value * 30
    elif time_unit == "years":
        time_limit = time_value * 365
    else:
        print("Invalid time unit. Defaulting to days.")
        time_unit = "days"
        time_limit = time_value

    # Ask for allowance and expenses
    allowance = int(input("Enter your allowance per day (THB): "))
    expenses = int(input("Enter your expenses per day (THB): "))

    daily_saving = allowance - expenses
    total_possible = daily_saving * time_limit
    required_daily = math.ceil(goal / time_limit)

    # RESULT
    if daily_saving <= 0:
        print("Your expenses are higher than your allowance.")
        print("Your goal is impossible to achieve.")

        # Ask to adjust goal or expenses
        adjust = input("Do you want to adjust your expenses or goal or NO: ").lower()
        if adjust == "expenses":
            cut = int(input("How much (THB) are you willing to cut from your daily expenses? "))
            daily_saving = (allowance - expenses) + cut
            if daily_saving > 0:
                total_possible = daily_saving * time_limit
                print(f"After cutting {cut} THB/day, your new daily saving is {daily_saving} THB.")
                print(f"You can now save {total_possible} THB in {time_value} {time_unit}.")
            else:
                print("Cutting that amount still isn't enough.")
        elif adjust == "goal":
            goal = total_possible
            print(f"New goal is {goal} THB (maximum possible with current allowance and expenses).")
        else:
            print("No changes made. Try again with adjusted allowance or expenses.")


    elif total_possible >= goal:
        print("Your goal is possible to achieve!")
        print(f"You need to save at least {required_daily} THB per day to reach your goal.")
        print(f"If you save the maximum ({daily_saving} THB/day),")
        print(f"you'll have {total_possible} THB saved after {time_value} {time_unit}.")
    else:
        print("Your goal is impossible to achieve with your current allowance and expenses.")
        adjust = input("Do you want to adjust your goal to the maximum possible saving? (yes/no): ").lower()

        if adjust == "yes":
            goal = total_possible
            print(f"🎯 New goal: {goal} THB (maximum possible in {time_value} {time_unit})")
            print(f"You need to save {daily_saving} THB/day to reach it.")
        else:
            print("You can try adjusting your expenses or extending your saving period.")



elif choice == "2":
    goal = int(input("Enter(in integer) amount of money(THB) you want to save: "))
    allowance = int(input("Enter(in integer) your allowance(THB) per day: "))
    expenses = int(input("Enter(in integer) your expenses(THB) per day: "))
    
    daily_saving_possible = allowance - expenses

    if daily_saving_possible <= 0:
        print("Your expenses are higher than your allowance.")
        print("Your goal is impossible to achieve")
        adjust = input("Do you want to adjust your expenses to reach the goal? (yes/no): ")

        if adjust.lower() == "yes":
            cut_amount = int(input("Enter(in integer) how much money(THB) you are willing to cut: "))
            new_expenses = expenses - cut_amount
            
            if new_expenses >= allowance:
                print("Cut amount is not enough.")
            elif int(new_expenses) < 0:
                print("Cut_amount is too large. Expenses can't be negative.")
            else:
                new_daily_saving = allowance - new_expenses
                number_of_days_required = math.ceil(goal / new_daily_saving)
                print(f"After cutting {cut_amount} THB per day,")
                print(f"you will reach your goal in {number_of_days_required} days.")
      
    else:
        number_of_days_required = math.ceil(goal / daily_saving_possible)
        print(f"You will need {number_of_days_required} days to reach your goal.")
else:
    print("Invalid input.")