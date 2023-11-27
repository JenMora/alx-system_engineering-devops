#!/usr/bin/python3
"""
Retrieves information about all employees' todo list progress
using the https://jsonplaceholder.typicode.com API.
"""

import json
import requests


def fetch_all_users():
    """
    Fetches information about all users from the API.

    Returns:
        list: A list of dictionaries containing details about each user.
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    user_dict = {}
    username_dict = {}

    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        username_dict[user_id] = user.get("username")

    return user_dict, username_dict


def fetch_all_tasks():
    """
    Fetches information about all tasks from the API.

    Returns:
        list: A list of dictionaries representing tasks for all users.
    """
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos",
                         verify=False).json()
    return tasks


def export_all_to_json():
    """
    Fetches information about all users and tasks,
    hen saves it to a JSON file.

    The JSON file is named 'todo_all_employees.json' and contains details
    about all employees' todo list progress.
    """
    user_dict, username_dict = fetch_all_users()
    tasks_info = fetch_all_tasks()

    for task in tasks_info:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username_dict.get(user_id)
        user_dict.get(user_id).append(task_dict)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(user_dict, json_file)


if __name__ == "__main__":
    export_all_to_json()
