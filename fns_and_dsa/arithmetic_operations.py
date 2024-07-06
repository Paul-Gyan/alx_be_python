# This function adds two numbers
def perform_operation(num1, num2, operation):
    return num1 + num2

# This function subtracts two numbers
def perform_operation(num1, num2,operation):
    return num1 - num2

# This function multiplies two numbers
def perform_operation(num1, num2,operation):
    return num1 * num2

# This function divides two numbers
def perform_operation(num1, num2,operation):
    return num1 / num2


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    operation = input("Enter operation:(1/2/3/4): ")

    # check if choice is one of the four options
    if operation in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operation == '1':
            print(num1, "+", num2, "=", perform_operation(num1, num2,operation))

        elif operation == '2':
            print(num1, "-", num2, "=", perform_operation(num1, num2,operation))

        elif operation == '3':
            print(num1, "*", num2, "=", perform_operation(num1, num2))

        elif operation == '4':
            print(num1, "/", num2, "=", perform_operation(num1, num2,operation))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")