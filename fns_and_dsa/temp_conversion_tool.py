FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        user_input = input("Enter a temperature (e.g., 32F or 20C): ")
        if user_input[-1].lower() == 'f':
            temperature = float(user_input[:-1])
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is approximately {converted_temp:.2f}°C")
        elif user_input[-1].lower() == 'c':
            temperature = float(user_input[:-1])
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is approximately {converted_temp:.2f}°F")
        else:
            raise ValueError("Invalid temperature format. Please enter a numeric value followed by 'F' or 'C'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value followed by 'F' or 'C'.")

if __name__ == "__main__":
    main()