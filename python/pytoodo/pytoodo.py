import os
import platform
import sys

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def add_task():
    clear_screen()
    display_header()
    display_tasks()
    task = input("\nEnter your task:\n> ")
    with open("pytasks.txt", "a") as file:
        file.write(f"{task}\n")
    print("Task added successfully!")

def delete_task():
    clear_screen()
    display_header()
    display_tasks()
    task_index = False
    while task_index is False:
        try:
            task_index = int(input("\nEnter the number of the task you want to delete: "))
        except Exception:
            clear_screen()
            display_header()
            display_tasks()
            continue
        
    with open("pytasks.txt", "r") as file:
        tasks = file.readlines()
    tasks = [task for task in tasks if task.strip()]
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number. Try again.")
        return
    with open("pytasks.txt", "w") as file:
        for i, task in enumerate(tasks, 1):
            if i != task_index:
                file.write(f"{task}")
    print("Task deleted successfully!")

def display_header():
    ver = "0.1.1"
    app_ver= f"[Version {ver}]"
    app_title = "Pytoodo"
    
    length = 28
    header = f"{app_title} | {app_ver}"
    
    print(""+"="*length)
    print(header)
    print(""+"="*length)
    
def display_choices():
        print("\nChoices: ")
        print("[1] - Show all tasks")
        print("[2] - Add task")
        print("[3] - Delete task")
        print("[q] - Quit")

def main():
    display_header()
    while True:
        clear_screen()
        display_header()    
        display_tasks()
        display_choices()
        choice = input("Enter your choice [1-3, q(uit)]\n> ")
        
        if choice == "1":
            clear_screen()
            display_header()
            display_tasks()

        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice.upper() == "Q":
            clear_screen()
            sys.exit()
        else:
            display_header()
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()