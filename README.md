# Task Tracker CLI

A simple command-line application to manage your tasks. Each task has a unique ID, description, status, and timestamps for creation and updates.

## Features
- Add new tasks
- List all tasks
- Update task description or status
- Delete tasks
- Track when tasks are created and updated

## How to Use

1. **Run the program**
   ```
   python main.py
   ```

2. **Menu Options**
   - Add Task: Enter a description to create a new task.
   - List Tasks: View all tasks with details.
   - Update Task: Enter the task ID to change its description or status.
   - Delete Task: Enter the task ID to remove it.
   - Exit: Quit the program.

## Task Fields
- **id**: Unique identifier for each task
- **description**: Short text about the task
- **status**: Task state (`todo`, `in-progress`, `done`)
- **createdAt**: Date and time when the task was created
- **updatedAt**: Date and time when the task was last updated

## Requirements
- Python 3.x

## Example
```
Task Tracker CLI
1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: 1
Enter task description: Buy groceries
Task added!
```


