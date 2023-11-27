#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import csv
import requests
from sys import argv

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_employee_info(employee_id):
    url = f"{BASE_URL}/users/{employee_id}"
    response = requests.get(url, verify=False)
    return response.json()


def get_tasks_info(employee_id):
    url = f"{BASE_URL}/todos?userId={employee_id}"
    response = requests.get(url, verify=False)
    return response.json()


def info_to_csv():
    employee_id = argv[1]

    user_info = get_employee_info(employee_id)
    tasks_info = get_tasks_info(employee_id)

    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks_info:
            task_writer.writerow([
                int(employee_id),
                user_info.get('username'),
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    info_to_csv()
