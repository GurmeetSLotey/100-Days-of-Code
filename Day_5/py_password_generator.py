import string
import random as r

symbols = list(string.punctuation)

# a-z and A-Z
letters = list(string.ascii_lowercase + string.ascii_uppercase)

# 0-9
numbers = list(string.digits)

print("Welcoem to the PyPassword Generator!")

num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))

password = []

for i in range(num_of_letters):
    password.append(r.choice(letters))

for i in range(num_of_symbols):
    password.append(r.choice(symbols))

for i in range(num_of_numbers):
    password.append(r.choice(numbers))

print(password)
r.shuffle(password)
password = "".join(password)
print(f"Your password is: {password}")