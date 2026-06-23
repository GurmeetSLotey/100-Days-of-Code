import calculator_art as art

def initalize():
    global num1
    global num2
    global operation
    global start

# define operations as functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def print_operations_text():
    return input("+\n" \
    "-\n" \
    "*\n" \
    "/\n" \
    "Pick an operation: ")


print(art.calculator_art)
# print("Starting")

operation_dic = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while True:
    num1 = float(input("What's the first number?: "))

    while True:
        operation = print_operations_text()
        num2 = float(input("What's the next number?: "))

        # print(operation_dic[operation])

        total = operation_dic[operation](num1 = num1, num2 = num2)

        print(f"{num1} {operation} {num2} = {total}")
        cont = input(f"Type 'y' to continue calculation with {total}, or type 'n' to start a new calculation:\n")
        num1 = total

        if cont != 'y':
            break

# get users first number

# get users operation

# execute operation

# ask user if they would like to continue with the calculated # or start over