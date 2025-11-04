import math

print("SAVING PLANNER APP :)")
print("Type 1 to check if your save up goal is possible in a given time")
print("Type 2 to calculate days needed to reach a goal")
choice = input("Enter 1 or 2: ")

if choice == "1":
    goal = int(input("Enter(in integer) amount of money(THB) you want to save: "))
    time_limit = int(input("Enter(in integer) time limit in days: "))
    if time_limit <= 0:
        print("Time limit must be at least 1 day.")
    else: 
        allowance = int(input("Enter(in integer) your allowance(THB) per day: "))
        expenses = int(input("Enter(in integer) your expenses(THB) per day: "))

        daily_saving_possible = allowance - expenses
        if daily_saving_possible <= 0:
            print("""You can't save any money because either your expenses is more than allowance or they are equal.""")
        else:
            total_possible = daily_saving_possible * time_limit
            required_daily_saving = math.ceil(goal / time_limit)

            if total_possible >= goal:
                print("Your goal is possible to achieve")
                print(f"You need to save at least {required_daily_saving} THB per day to reach your goal.")
                print(f"""The maximum amount of money you can save is {total_possible} if you save {daily_saving_possible}.""")
            else:
                print("Your goal is impossible to achieve with current allowance/expenses.")

                adjust = input("Do you want to adjust your goal to maximum possible saving? (type yes or no): ")
        
                if adjust.lower() == "yes":
                    goal = total_possible
                    required_daily_saving = math.ceil(goal / time_limit)
                    print(f"New goal: {goal}")
                    print(f"You need to save {required_daily_saving} per day to reach it.")  
                elif adjust.lower() == "no":
                    adjust = input("Do you want to adjust your expenses to reach the goal? (yes/no): ")
                    if adjust.lower() == "yes":
                        cut_amount = int(input("Enter(in integer) how much money(THB) you are willing to cut: "))
                        new_expenses = expenses - cut_amount
                        if new_expenses >= allowance:
                            print("Cut amount is not enough.")
                        elif new_expenses < 0:
                            print("Cut amount is too large. Expenses can't be negative.")
                        else:
                            new_daily_saving = allowance - new_expenses
                            number_of_days_required = math.ceil(goal / new_daily_saving)
                            print(f"After cutting {cut_amount} THB per day,")
                            print(f"you will reach your goal in {number_of_days_required} days.")
                    else:
                        print("You refused to adjust. Bye")
                else:
                    print("You didn't type yes or no")

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