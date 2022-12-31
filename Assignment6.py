import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
    
    def __str__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# Read the JSON file
with open('employee.json', 'r') as f:
    data = json.load(f)

# Create a list of Employee objects
employees = []
for employee in data:
    name = employee['Name']
    dob = employee['DOB']
    height = employee['Height']
    city = employee['City']
    state = employee['State']
    employees.append(Employee(name, dob, height, city, state))

# Print the list of Employee objects
for employee in employees:
    print(employee)
