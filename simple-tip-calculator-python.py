print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

calculated_tip = tip / 100 * bill
total_price = bill + calculated_tip
total_price_for_each_person = round(total_price / people , 2)
print(f"Each person should pay: $ {total_price_for_each_person}")




