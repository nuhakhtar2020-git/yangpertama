def show_menu():
    print("\n--- DAILY ORGANIZER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                with open("tasks.txt", "r") as file:
                    print("\nYOUR TASKS:")
                    print(file.read())
            except FileNotFoundError:
                print("\nNo tasks found. Add one first!")

        elif choice == '2':
            task = input("Enter the task: ")
            with open("tasks.txt", "a") as file:
                file.write(f"- {task}\n")
            print("Task saved!")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
