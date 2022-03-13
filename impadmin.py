class User():
    def __init__(self, first_name, last_name, username, number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.number = number
        self.login_attempts = 0
    def describe_user(self):
        print("User: " + self.first_name + self.last_name)
        print("Username: " + self.username + self.number)
    def welcome_user(self):
        print("Welcome " + self.username + "!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, number):
        super().__init__(first_name, last_name, username, number)
        self.privileges = Privliges()
class Privliges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print("Admins can: ")
        if self.privileges:
            for privilege in self.privileges:
                print(" : " + privilege)

privileges = [
    'Can reset passwords',
    'Can moderate discussions',
    'Can suspend accounts',
    ]

li = Privliges