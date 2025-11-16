task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

print(f"Reminder: {reminder}")
