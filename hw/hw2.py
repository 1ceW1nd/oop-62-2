class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def get_role(self):
        return "Employee"

    def get_info(self):
        return f"Имя: {self.name} | Роль: {self.get_role()} | Зарплата: {self.get_salary()}"



class BackendDeveloper(Employee):
    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self.level = level

    def get_salary(self):
        if self.level == "junior":
            return self.salary
        elif self.level == "middle":
            return int(self.salary * 1.2)
        elif self.level == "senior":
            return int(self.salary * 1.5)
        return self.salary

    def get_role(self):
        return "BackendDeveloper"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_salary(self):
        return self.salary + self.team_size * 1000

    def get_role(self):
        return "Manager"


class Intern(Employee):
    def __init__(self, name, salary, months):
        super().__init__(name, salary)
        self.months = months

    def get_salary(self):
        return 10000

    def get_role(self):
        return "Intern"



def print_salary(employees):
    for emp in employees:
        print(emp.get_info())



if __name__ == "__main__":

    emp = Employee("Alex", 30000)
    print(emp.get_info())
    print()

    employees = [
        BackendDeveloper("Artem", 40000, "middle"),
        Manager("Oleg", 50000, 5),
        Intern("Ivan", 20000, 3),
    ]

    print_salary(employees)
    print()

    developers = [
        BackendDeveloper("Junior Dev", 30000, "junior"),
        BackendDeveloper("Middle Dev", 40000, "middle"),
        BackendDeveloper("Senior Dev", 50000, "senior"),
    ]

    print("Разработчики разных уровней:")
    print_salary(developers)