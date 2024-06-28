task = input('Enter your task: ')
priority = input("Priority (high / medium / low): ").lower()
time_bound = input("Is it time-bound (yes / no): ").lower()

match priority:
    case "high":
        print(f'High Priority.')
    case "medium":
        print(f'Medium Priority.')
    case "low":
        print(f'Low priority.')
if time_bound.lower() == 'yes':
    print(f'That requires a immediate action today!')
else:
    print(f'You are good to go.')