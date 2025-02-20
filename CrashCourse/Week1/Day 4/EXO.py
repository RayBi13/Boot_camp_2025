class Employee:
    def __init__(self, firstname, lastname, age, job, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary

    def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount

    def display_info(self):
        print(f"{self.firstname} {self.lastname}, {self.age} years old, {self.job}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, firstname, lastname, age, job="developer", salary=15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.coding_skills = []

    def add_skills(self, *skills):
        self.coding_skills.extend(skills)

    def coding(self):
        print(f"{self.firstname} knows the following coding languages: {', '.join(self.coding_skills)}")

    def coding_with_partner(self, other_developer):
        print(f"{self.firstname} and {other_developer.firstname} know the following coding languages: {', '.join(self.coding_skills + other_developer.coding_skills)}")

    def get_promotion(self, promotion_amount):
        self.salary *= promotion_amount

class Manager(Employee):
    def __init__(self, firstname, lastname, age, job="manager", salary=15000):
        super().__init__(firstname, lastname, age, job, salary)
        self.employees = []

    def add_new_employee(self, new_employee):
        self.employees.append(new_employee)

    def show_employees(self):
        for employee in self.employees:
            print(f"{employee.firstname} {employee.lastname}")

# Creer l'objet developpeur
dev1 = Developer("Tom", "Cruiz", 30)
dev2 = Developer("Angelina", "Jolie", 23)

# creer leurs attributs
dev1.display_info()
dev2.display_info()

# Add skills to developers
dev1.add_skills("Python", "Java")
dev2.add_skills("JavaScript", "C++")

# Call coding methods
dev1.coding()
dev2.coding()
dev1.coding_with_partner(dev2)

# Call get_promotion method
dev1.get_promotion(1.1)
dev1.display_info()

# Create Manager object
manager = Manager("Brad", "Pitt", 50)

# Display manager's attributes
manager.display_info()

# Add employees to manager
manager.add_new_employee(dev1)
manager.add_new_employee(dev2)

# Show employees under manager
manager.show_employees()

































