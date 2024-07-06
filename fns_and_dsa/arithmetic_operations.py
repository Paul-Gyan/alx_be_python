def perform_operation(num1, num2):
	return num1 +  num2

	return num1 - num2

	return num1 / num2

	return num1 * num2

print("Select operation")
print("1.add")
print("2.subtract")
print("3.divide")
print("4.multiply")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Result:", perform_operation(num1, num2))

        elif choice == '2':
            print("Result:", perform_operation(num1, num2))

        elif choice == '3':
        	if num2 == 0:
        		print("Error, cannot divide by zero.")
        	else:
        		print("Result:", perform_operation(num1, num2))

            

        elif choice == '4':
            print("Result:", perform_operation(num1, num2))
        
        
    else:
        print("Invalid Input")