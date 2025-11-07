tasks = [
    "task 1",
    "task 2",
    "task 3",
    "task 4",
    "task 5",
    "task 6",
    "task 7",
    "task 8"
]

# tasks.append("Go to home") # hard-coded value
# tasks.append(input("Enter Task: "))


# while True:
#     user_input = input("Enter Task: ")

#     if user_input == "":
#         print("User input was empty!")
#         break
#     else:
#         if user_input in tasks:
#             print("This task was repeated")
#             continue
        
#         tasks.append(user_input)
    # print("End of iteration")

# if tasks.count("Go to home") > 1:
# print(tasks.count("Go to home"))
# print("help" in tasks)
print(tasks)

todays_task_count = 4
todays_tasks = tasks[0:todays_task_count]

# print(tasks[0:todays_task_count])

total_time = 0

for task in todays_tasks:
    while True:
        try:
            user_input = int(input(f"How many minutes to {task}? "))

            if user_input > 0:
                total_time += user_input
                break
            print("Please enter non-negative time!")
        except ValueError:
            print("Please Enter correct number!")


print(f"You need {total_time} minutes to finish all tasks")

avg = total_time / todays_task_count
# print(avg)
print(f"You need {avg:.1f} minutes for each task on average")
