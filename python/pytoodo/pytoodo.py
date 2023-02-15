import os
import platform
import sys
import datetime

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_line_art(title_bar_msg: str) -> str:
    # set [1-4]
    style = 4
    # len of header
    number = 20
    
    if style == 1:
        # >>--------------->
        string = f">>" + "-"*number + ">"    
    elif style == 2:
        # :.:.:.:.:.:.:.:.:.:.:
        string = f":."*number + ":"
    elif style == 3:
        # @-->--->--->--->--->--->--->--->--->--->--->
        string = f"@--" + ">---"*number + ">"
    elif style == 4:
        # ----------------------
        string = f"-"*number
    else:
        string = []
    string = title_bar_msg + "\n" + string
    return string

def display_tasks():
    if not os.path.exists("pytasks.txt") or os.stat("pytasks.txt").st_size == 0:
        print("You have no tasks for today! Try adding some tasks below.")
        return

    with open("pytasks.txt", "r") as file:
        print("Your current tasks:")
        tasks = file.readlines()
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")


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
    print(display_line_art("owo"))
   
def display_choices():
        print("\nChoices: ")
        print("[1] - Show all tasks")
        print("[2] - Add task")
        print("[3] - Delete task")
        print("[q] - Quit")

def dislay_main_menu():
        clear_screen()
        display_header()    
        display_tasks()
        
def main():
    while True:
        dislay_main_menu()
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