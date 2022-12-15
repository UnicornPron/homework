class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary
    def work(self):
        return "I come to the office."
    def __str__(self):
       return f'position is: {self.name}'
    def check_salary(self, days):
       return self.daily_salary * days

class Recruiter(Employee):
    def work(self):
        return super(Recruiter, self).work()[:-1] + " and start to hiring."

class Developer(Employee):
    def work(self):
        return super(Developer, self).work()[:-1] + " and start to coding."
    def __init__(self, name, daily_salary, tech_stack):
        self.name = name
        self.daily_salary = daily_salary
        self.tech_stack = tech_stack
        self.tech = []
    def __gt__(self, other):
        return self.tech_stack > other.tech_stack

worker1 = Recruiter('Vasya', 500)
worker2 = Developer('Kolya', 1000, python)
worker3 = Developer('Alex', 1100, djanga)

print(worker2>worker3)