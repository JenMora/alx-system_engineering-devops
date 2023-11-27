#!/usr/bin/python3
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # API endpoint
    base_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{base_url}/{employee_id}/todos"

    # Fetching employee information
    response_employee = requests.get(f"{base_url}/{employee_id}")
    employee_data = response_employee.json()
    employee_name = employee_data['name']

    # Fetching employee's TODO list
    response_todo = requests.get(todo_url)
    todos = response_todo.json()

    # Counting completed tasks
    completed_tasks = [task for task in todos if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Displaying progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}): ")

    # Displaying completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
