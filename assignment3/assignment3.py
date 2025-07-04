import pandas as pd
import os

#Task 1: Introduction to Pandas - Creating and Manipulating DataFrames

    # 1.Create a DataFrame from a dictionary:

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)

print(task1_data_frame)

    # 2. Add a new column:

task1_with_salary = task1_data_frame.copy()

task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

    # 3. Modify an existing column:

task1_older = task1_with_salary.copy()

task1_older['Age'] = task1_older['Age']+1

print(task1_older)

    # 4. Save the DataFrame as a CSV file:

task1_older.to_csv('employees.csv', index=False)

with open('employees.csv', 'r') as file:

    print(file.read())

#Task 2: Loading Data from CSV and JSON

    # 1. Read data from a CSV file:

task2_employees = pd.read_csv('employees.csv')

print(task2_employees)

    # 2. Read data from a JSON file:

additional_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

df = pd.DataFrame(additional_data)

df.to_json('additional_employees.json', orient='records', indent=4)

with open ('additional_employees.json', 'r') as file:

    json_employees = pd.read_json(file)

print(json_employees)

    # 3. Combine DataFrames:

#Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable more_employees.

more_employees = pd.concat([task2_employees, json_employees], ignore_index = True)

print(more_employees)


#Task 3: Data Inspection - Using Head, Tail, and Info Methods

    # 1.Use the head() method:

first_three = more_employees.head(3)   

print(first_three)

    # 2. Use the tail() method:

last_two = more_employees.tail(2)

print(last_two)

    # 3. Get the shape of a DataFrame

shape_employee = more_employees.shape

print(shape_employee)

    # 4. Use the info() method:

info_employees = more_employees.info()

print(info_employees)

#Task 4: Data Cleaning 

    # 1Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.

with open('assignment3/dirty_data.csv', 'r') as file:
    dirty_data = pd.read_csv(file)

print(dirty_data)

clean_data = dirty_data.copy()

    #2. Remove any duplicate rows from the DataFrame

clean_data = clean_data.drop_duplicates()

print(clean_data)

    # 3. Convert Age to numeric and handle missing values

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

print(clean_data['Age'])

    # 4. Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN

clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce').replace(['unknown', 'n/a'], pd.NA)

print (clean_data['Salary'])

    # 5. Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median

clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
print(clean_data['Age'])

clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data['Salary'])


    # 6. Convert Hire Date to datetime

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors = 'coerce')
print(clean_data["Hire Date"])

    # 7. Strip extra whitespace and standardize Name and Department as uppercase

clean_data = clean_data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

clean_data['Name'] = clean_data['Name'].str.upper()

clean_data['Department'] = clean_data['Department'].str.upper()


print(clean_data)

