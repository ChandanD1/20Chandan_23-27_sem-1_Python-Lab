# Write a program to Create Employee Class & add methods to get employee details & print.

class Employee:
    def __init__(self, emp_id, name, gender, city, salary):
        self.emp_id = emp_id
        self.name = name
        self.gender = gender
        self.city = city
        self.salary = salary

def main():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    city = input("Enter City: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(emp_id, name, gender, city, salary)

    print("\nEmployee Details:")
    print("ID:", employee.emp_id)
    print("Name:", employee.name)
    print("Gender:", employee.gender)
    print("City:", employee.city)
    print("Salary:", employee.salary)

if __name__ == "__main__":
    main()