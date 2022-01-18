# Calculator
# Made by Dean Mysliwiec

# add function
def add(n1, n2):
    return n1 + n2


# multiply function
def multiply(n1, n2):
    return n1 * n2


# subtract function
def subtract(n1, n2):
    return n1 - n2


# divide function
def divide(n1, n2):
    return n1 / n2


# operations that can be used
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# get number 1 from user
num1 = float(input("What's the first number?: "))

# list operations user can do
for operate in operations:
    print(f"{operate}")
# ask user what operation they want to do
operation_symbol = input("Pick an operation from the line above: ")
# ask user for second number
num2 = float(input("What's the second number?: "))

# calculation_function based on operations values in dictionary
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

# output answer
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# for loop through
previous_answer = first_answer

# ask user if they want to continue calculating with previous answer
again = input(f"Would you like to continue calculating w/ {previous_answer} (Y for Yes or N for New or E to End): ").lower()
# start loop as long as again doesn't equal e
while again != "e":
    if again == "n":
        # fresh start with new numbers if user chooses so
        previous_answer = float(input("What's the first number?: "))
        print(previous_answer)
    # user picks operation symbol again
    operation_symbol = input("Pick another operation: ")
    # asks for users next number
    num3 = float(input("What's the next number?: "))
    # set up calculation_function again
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(previous_answer, num3)
    # get new answer
    print(f"{previous_answer} {operation_symbol} {num3} = {second_answer}")
    # set new answer as the previous answer for loop through again if user chooses to do so
    previous_answer = second_answer
    # ask user what they want to do
    again = input(f"Would you like to continue calculating w/ {previous_answer} (Y for Yes or N for New or E to End): ").lower()