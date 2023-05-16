class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

# Create a task manager instance
task_manager = TaskManager()

# Add tasks to the task manager
task1 = Task("Finish project", "Complete the final report", "High")
task_manager.add_task(task1)

task2 = Task("Send email", "Follow up with clients", "Medium")
task_manager.add_task(task2)

task3 = Task("Buy groceries", "Milk, eggs, and bread", "Low")
task_manager.add_task(task3)

# Get all tasks
all_tasks = task_manager.get_all_tasks()
print("All tasks:")
for task in all_tasks:
    print(f"Title: {task.title}, Priority: {task.priority}")

# Get tasks with high priority
high_priority_tasks = task_manager.get_tasks_by_priority("High")
print("\nHigh priority tasks:")
for task in high_priority_tasks:
    print(f"Title: {task.title}, Description: {task.description}")

# Remove a task
task_manager.remove_task(task2)

# Get all tasks again
all_tasks = task_manager.get_all_tasks()
print("\nAll tasks after removing a task:")
for task in all_tasks:
    print(f"Title: {task.title}, Priority: {task.priority}")
