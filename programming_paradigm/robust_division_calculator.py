def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        else:
            return f"The result of the division is {numerator / denominator}".strip()
    except ValueError:
        return "Error: Please enter numeric values only."