import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2: Read a CSV File 
def read_employees():
    data = {}
    rows = []

    try:
        with open("../csv/employees.csv") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)

        data["rows"] = rows
        return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f'File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Code: {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

employees = read_employees()
print(employees)


# Task 3: Find the Column Index

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
print (employee_id_column)


# Task 4: Task 4: Find the Employee First Name
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

print(first_name(0))

# Task 5: Find the Employee: a Function in a Function

def employee_find(employee_id):
    def employee_match(row):    
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find(1))

# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

print(employee_find_2(1)) 

# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    index = column_index("last_name")  
    employees["rows"].sort(key=lambda row: row[index])  
    return employees["rows"] 

print(sort_by_last_name()) 

# Task 8: Create a dict for an Employee

def employee_dict(row):
    result = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":  
            result[field] = row[i]
    return result
print(employee_dict(employees["rows"][5]))

# Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]  # берём employee_id как ключ
        result[emp_id] = employee_dict(row)  # значение — словарь сотрудника
    return result

print(all_employees_dict())
# Task 10: Use the os Module

def get_this_value():
    return os.getenv("THISVALUE")

print(get_this_value()) 

# Task 11: Creating Your Own Module

def set_that_secret(secret):
    custom_module.set_secret(secret)

set_that_secret("bumbum")  
print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv

def read_minutes():
    def load_minutes(path):
        result = {}
        rows = []

        with open(path, "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    result["fields"] = row
                else:
                    rows.append(tuple(row))

        result["rows"] = rows
        return result

    minutes1 = load_minutes("../csv/minutes1.csv")
    minutes2 = load_minutes("../csv/minutes2.csv")

    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: Create minutes_set

def create_minutes_set():
    set1 = set(minutes1["rows"])  
    set2 = set(minutes2["rows"])  
    combined = set1.union(set2)   
    return combined

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: Convert to datetime

def create_minutes_list():
    raw_list = list(minutes_set)  

    
    converted = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), raw_list)

    result = list(converted) 
    result.sort(key=lambda x: x[1])  
    return result

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: Write Out Sorted List

def write_sorted_list():
    
    minutes_list.sort(key=lambda x: x[1])

    
    formatted_list = list(map(
        lambda x: (x[0], x[1].strftime("%B %d, %Y")),
        minutes_list
    ))

    
    with open("../minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        
        writer.writerow(minutes1["fields"])

        
        writer.writerows(formatted_list)

    return formatted_list

written_minutes = write_sorted_list()
print(written_minutes)

