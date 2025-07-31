#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Comandos
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": get_timestamp(),
        "updatedAt": get_timestamp()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        print(f"[{t['id']}] ({t['status']}) - {t['description']}")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = get_timestamp()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == len(new_tasks):
        print("Task not found.")
        return
    save_tasks(new_tasks)
    print("Task deleted successfully")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = get_timestamp()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found.")

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Please provide a task description")
        else:
            add_task(sys.argv[2])

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task-cli update <id> <new description>")
        else:
            update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <id>")
        else:
            delete_task(int(sys.argv[2]))

    elif command == "mark-done":
        mark_task(int(sys.argv[2]), "done")

    elif command == "mark-in-progress":
        mark_task(int(sys.argv[2]), "in-progress")

    else:
        print("Unknown command")
