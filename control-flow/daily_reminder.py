Task = input("Please enter the task:")
Time = input("Is it time-bound? (yes/no)?").lower()
Priority = input("Please enter the task priority(high/medium/low):")

match task_priority:
    case _ if task_priority == "high":
        print("Reminder:'",task, "'is a high priority task that requres immediate attention today!")
    case _ if task_priority == "medium":
        print("Reminder:'",task, "'is a medium priority task that requres immediate attention today!")
    case _ if task_priority == low:
        print("Note:'", task ,"'is a low is a low priority task. Consider completing it when you have free time.")

