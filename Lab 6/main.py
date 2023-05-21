class Employee:
    def __init__(self, position, salary):
        self.position = position
        self.salary = salary


class Department:
    def __init__(self, employees):
        self.employees = employees

    def get_salary_report(self):
        salary_report = []
        for employee in self.employees:
            salary_report.append((employee.position, employee.salary))
        return salary_report


class Company:
    def __init__(self, departments):
        self.departments = departments

    def get_salary_report(self):
        salary_report = []
        for department in self.departments:
            salary_report.extend(department.get_salary_report())
        return salary_report

# Створення співробітників
employee1 = Employee("Менеджер", 12000)
employee2 = Employee("Аналітик", 10000)
employee3 = Employee("Розробник", 11000)

# Створення департаментів зі співробітниками
department1 = Department([employee1, employee2])
department2 = Department([employee3])

# Створення компанії з департаментами
company = Company([department1, department2])

# Репорт для всієї компанії
salary_report_company = company.get_salary_report()
print("Репорт для компанії:")
for position, salary in salary_report_company:
    print(f"Посада: {position}, Зарплата: {salary}")

# Репорт для окремого департаменту
department_report = department1.get_salary_report()
print("Репорт для департаменту:")
for position, salary in department_report:
    print(f"Посада: {position}, Зарплата: {salary}")