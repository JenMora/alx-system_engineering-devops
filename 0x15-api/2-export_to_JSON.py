#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import json
import requests
from sys import argv

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_employee_info(employee_id):
    """
    Retrieve employee information from the API.

    Parameters:
        employee_id (str): The ID of the employee.

    Returns:
        dict: A dictionary containing information about the employee.
    """
    url = f"{BASE_URL}/users/{employee_id}"
    response = requests.get(url, verify=False)
    return response.json()


def get_tasks_info(employee_id):
    """
    Retrieve tasks information for a given employee from the API.

    Parameters:
        employee_id (str): The ID of the employee.

    Returns:
        list: A list of dictionaries representing tasks for the employee.
    """
    url = f"{BASE_URL}/todos?userId={employee_id}"
    response = requests.get(url, verify=False)
    return response.json()


def info_to_json():
    """
    Retrieve employee and tasks information, and save it to a JSON file.

    The JSON file is named '{employee_id}.json' and contains information
    about the employee's todo list progress.
    """
    employee_id = argv[1]

    # Retrieve employee information
    user_info = get_employee_info(employee_id)

    # Retrieve tasks information
    tasks_info = get_tasks_info(employee_id)

    # Extract relevant details
    employee_username = user_info.get('username')
    employee_tasks = []

    # Prepare tasks data
    for task_info in tasks_info:
        task_dict = {
            "task": task_info.get('title'),
            "completed": task_info.get('completed'),
            "username": employee_username
        }
        employee_tasks.append(task_dict)

    # Create JSON object
    result_json = {employee_id: employee_tasks}

    # Save to JSON file
    with open(f"{employee_id}.json", 'w') as json_file:
        json.dump(result_json, json_file)


if __name__ == "__main__":
    info_to_json()
