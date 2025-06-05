# TASK 3: List Comprehensions Practice

import os
import pandas as pd

# Get the current directory (where this script is located)
current_dir = os.path.dirname(__file__)

# Build the path to the employees.csv file
csv_path = os.path.join(current_dir, "..", "python_homework", "csv", "employees.csv")

# Make path valid on all operating systems
csv_path = os.path.normpath(csv_path)

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# Use a list comprehension to create a list of full names
full_names = [f"{row['first_name']} {row['last_name']}" for _, row in df.iterrows()]
print("All employee names:")
print(full_names)

# Use another list comprehension to filter names that contain the letter 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nEmployee names containing the letter 'e':")
print(names_with_e)

