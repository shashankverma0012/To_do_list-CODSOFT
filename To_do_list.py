# todo_list.py

class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks = [line.strip() for line in f.readlines()]
            return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(task + '\n')

    def create_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, old_task, new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            self.save_tasks()

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

def main():
    todo_list = ToDoList('todo.txt')

    while True:
        print("\nTo-Do List Menu:")
        print("1. Create Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a new task: ")
            todo_list.create_task(task)
        elif choice == '2':
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            todo_list.update_task(old_task, new_task)
        elif choice == '3':
            task = input("Enter the task to delete: ")
            todo_list.delete_task(task)
        elif choice == '4':
            todo_list.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()