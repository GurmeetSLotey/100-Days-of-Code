print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))

# Later work on error handling by checking if the input from user was 10, 12 or 15
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))

num_of_people = int(input("How many people to split the bill? "))

cost_per_person = total/num_of_people
tip_amt = total * (tip_percent/100)
tip_per_person = tip_amt/num_of_people

# How to better get precision to two decimal places
print("Each person should pay: $" + str(round(cost_per_person + tip_per_person,2)))