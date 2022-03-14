class Employee():

    def __init__(self, first, last, ann_salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        self.ann_salary += amount