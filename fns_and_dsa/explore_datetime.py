from datetime import datetime, timedelta

def display_current_datetime():
  """
  Gets the current date and time and prints it in a readable format.
  """
  current_date = datetime.now()
  formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(days):
  """
  Calculates the future date by adding a specified number of days to the current date.

  Args:
      days: Number of days to add (integer).

  Returns:
      The future date as a datetime object.
  """
  current_date = datetime.now()
  future_date = current_date + timedelta(days=days)
  return future_date

def main():
  display_current_datetime()

  while True:
    try:
      days = int(input("Enter the numbers of days to add to the current date or 0 to exit"))
      if days == 0:
        break
      future_date = calculate_future_date(days)
      formatted_future_date = future_date.strftime("%Y-%m-%d")
      print(f"Date after {days} days: {formatted_future_date}")
    except ValueError:
      print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
  main()