task = input("Enter your task:")
Priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):").lower()


match Priority:
    case _ if Priority == "high":
        print("Reminder:",task,"is a high priority task that requres immediate attention today!")
    case _ if Priority == "medium":
        print("Reminder:",task,"is a medium priority task that requres immediate attention today!")
    case _ if Priority == "low":
        print("Note:'",task,"'is a low is a low priority task. Consider completing it when you have free time.")

