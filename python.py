class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def search_by_age(self, target_age):
        result = [emp for emp in self.employees if emp.age == target_age]
        return result

    def search_by_name(self, target_name):
        result = [emp for emp in self.employees if emp.name.lower() == target_name.lower()]
        return result

    def search_by_salary(self, condition, target_salary):
        if condition == ">":
            result = [emp for emp in self.employees if emp.salary > target_salary]
        elif condition == "<":
            result = [emp for emp in self.employees if emp.salary < target_salary]
        elif condition == ">=":
            result = [emp for emp in self.employees if emp.salary >= target_salary]
        elif condition == "<=":
            result = [emp for emp in self.employees if emp.salary <= target_salary]
        else:
            result = []
        return result

    def display_result(self, result):
        if not result:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary (PM)")
            for emp in result:
                print(f"{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

def main():
    emp_table = EmployeeTable()
    
    # Add employees to the table
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))
    
    while True:
        print("\nSearch Options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary (>, <, <=, >=)")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            target_age = int(input("Enter age to search: "))
            result = emp_table.search_by_age(target_age)
        elif choice == "2":
            target_name = input("Enter name to search: ")
            result = emp_table.search_by_name(target_name)
        elif choice == "3":
            condition = input("Enter condition (>, <, <=, >=): ")
            target_salary = float(input("Enter salary to search: "))
            result = emp_table.search_by_salary(condition, target_salary)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        emp_table.display_result(result)

if __name__ == "__main__":
    main()
