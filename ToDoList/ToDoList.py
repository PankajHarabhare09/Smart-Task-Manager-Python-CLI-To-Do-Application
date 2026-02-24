from datetime import datetime


class ToDoList:
    def __init__(self):
        self.file_name = "ToDoList.txt"
        self.tasks = []
        self.load_tasks()

    # -------------------------------
    # Load Tasks from File
    # -------------------------------
    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    # -------------------------------
    # Save Tasks to File
    # -------------------------------
    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    # -------------------------------
    # Add Task
    # -------------------------------
    def add_task(self):
        task_name = input("Enter the task: ").strip()
        if not task_name:
            print("Task cannot be empty.")
            return

        print("Select Priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        priority_choice = input("Enter choice (1-3): ").strip()

        if priority_choice == "1":
            priority = "High"
        elif priority_choice == "2":
            priority = "Medium"
        elif priority_choice == "3":
            priority = "Low"
        else:
            priority = "Low"

        due_date_input = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()

        if due_date_input:
            try:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
                formatted_date = due_date.strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. No due date set.")
                formatted_date = "No Date"
        else:
            formatted_date = "No Date"

        formatted_task = f"[ ] ({priority}) [{formatted_date}] {task_name}"
        self.tasks.append(formatted_task)
        self.save_tasks()
        print("Task added successfully.")

    # -------------------------------
    # Display Tasks (with Overdue)
    # -------------------------------
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTo-Do List:")
        today = datetime.today()

        for idx, task in enumerate(self.tasks, start=1):

            try:
                date_start = task.index("[", task.index("]") + 1) + 1
                date_end = task.index("]", date_start)
                due_date_str = task[date_start:date_end]

                if due_date_str != "No Date":
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

                    if today > due_date and task.startswith("[ ]"):
                        print(f"{idx}. {task}  ⚠ OVERDUE")
                    else:
                        print(f"{idx}. {task}")
                else:
                    print(f"{idx}. {task}")

            except:
                print(f"{idx}. {task}")

    # -------------------------------
    # Mark Task as Completed
    # -------------------------------
    def mark_task_completed(self):
        if not self.tasks:
            print("No tasks to mark.")
            return

        self.display_tasks()

        try:
            index = int(input("Enter task number to mark complete: "))
            if 1 <= index <= len(self.tasks):
                task = self.tasks[index - 1]

                if task.startswith("[x]"):
                    print("Task already completed.")
                else:
                    self.tasks[index - 1] = task.replace("[ ]", "[x]", 1)
                    self.save_tasks()
                    print("Task marked as completed.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    # -------------------------------
    # Remove Task
    # -------------------------------
    def remove_task(self):
        if not self.tasks:
            print("No tasks to remove.")
            return

        self.display_tasks()

        try:
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(self.tasks):
                removed = self.tasks.pop(index - 1)
                self.save_tasks()
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    # -------------------------------
    # Clear All Tasks
    # -------------------------------
    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()
        print("All tasks cleared.")

    # -------------------------------
    # Sort Tasks by Due Date
    # -------------------------------
    def sort_tasks_by_date(self):
        def extract_date(task):
            try:
                date_start = task.index("[", task.index("]") + 1) + 1
                date_end = task.index("]", date_start)
                due_date_str = task[date_start:date_end]

                if due_date_str == "No Date":
                    return datetime.max

                return datetime.strptime(due_date_str, "%Y-%m-%d")
            except:
                return datetime.max

        self.tasks.sort(key=extract_date)
        self.save_tasks()
        print("Tasks sorted by due date.")

    # -------------------------------
    # Main Menu
    # -------------------------------
    def main(self):
        while True:
            print("\n====== TO-DO LIST MENU ======")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Display Tasks")
            print("4. Clear All Tasks")
            print("5. Mark Task as Completed")
            print("6. Sort Tasks by Due Date")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.remove_task()
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                self.clear_tasks()
            elif choice == "5":
                self.mark_task_completed()
            elif choice == "6":
                self.sort_tasks_by_date()
            elif choice == "7":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Try again.")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    todo = ToDoList()
    todo.main()