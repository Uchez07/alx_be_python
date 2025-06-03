Task = input("Please enter the task:")
Priority = input("Please enter the task priority(high/medium/low):")
Time_Bound = input("Is it time-bound? (yes/no)?").lower()


match Priority:
    case _ if Priority == "high":
        print("Reminder:'",Task, "'is a high priority task that requres immediate attention today!")
    case _ if Priority == "medium":
        print("Reminder:'",Task, "'is a medium priority task that requres immediate attention today!")
    case _ if Priority == "low":
        print("Note:'",Task,"'is a low is a low priority task. Consider completing it when you have free time.")

