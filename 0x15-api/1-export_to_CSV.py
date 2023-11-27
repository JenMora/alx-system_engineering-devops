#!/usr/bin/python3
"""
This is a script that Uses REST API for a given employee ID to return
information about his/her TODO list progress
"""


import requests
import sys
import cv


def todo_list(employee_id):
    """
    This method returns information about an employee's TODO list
    """
    url_api = f'https://jsonplaceholder.typicode.com/'\
              f'todos?userId={employee_id}'
    try:
        response = requests.get(url_api)
        response.raise_for_status()
        todo = response.json()
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/'
                                     f'users/{employee_id}')
        user_response.raise_for_status()
        user_info = user_response.json()
        employee_name = user_info['name']
        completed_tasks = []
        for task in todo:
            if task['completed']:
                completed_tasks.append(task)
        total_tasks = len(todo)
        completed_task_num = len(completed_tasks)
        print(f"Employee {employee_name} is done with tasks"
              f"({str(completed_task_num)}/{str(total_tasks)}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def export_csv(employee_id, total_tasks, tasks, user_info):
    """
    Export data in CSV format.

    Parameters:
        employee_id (str): The ID of the employee for whom tasks
        are being exported.
        total_tasks (int): The total number of tasks.
        tasks (list): A list of dictionaries representing tasks,each containing
        'completed' and 'title' keys.
        user_info (dict): A dictionary containing user information,
        including the 'username'.

    Returns:
        None

    Generates a CSV file named '{employee_id}.csv' with the following columns:
        - USER_ID: The employee ID.
        - USERNAME: The username associated with the employee.
        - TASK_COMPLETED_STATUS: The completion status of each task.
        - TASK_TITLE: The title of each task.
    """

    file_name = f"{employee_id}.csv"

    with open(file_name, 'w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)
        for task in tasks:

            csv_writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': user_info['username'],
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        todo_list(employee_id)
    except ValueError as e:
        print(e)
        sys.exit(1)
