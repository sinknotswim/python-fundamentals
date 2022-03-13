#9-6

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name + " serves the best " + self.cuisine_type + ".")
    def open_restaurant(self):
        print(self.restaurant_name + " is open!")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="ice_cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []
    def show_flavors(self):
        print("Look at our menu flavors: ")
        for flavor in self.flavors:
            print(" : " + flavor)

cream = IceCreamStand("Cold Stone")
cream.flavors = ["Vanilla", "Chocolate", "Mint Chocolate Chip"]
cream.show_flavors()

#9-7

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
        self.privileges = []
    def show_privileges(self):
        print("Admins can: ")
        for privilege in self.privileges:
            print(" : " + privilege)


li = Admin("Li ", "Taylor ", "sinknotswim", "#1720")
li.describe_user()

li.privileges = [
    'Can reset passwords',
    'Can moderate discussions',
    'Can suspend accounts',
    ]

li.show_privileges()

#9-8

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

li = Admin("Li ", "Taylor ", "sinknotswim", "#1720")
li.describe_user()

li.privileges = [
    'Can reset passwords',
    'Can moderate discussions',
    'Can suspend accounts',
    ]
#horse
class Horse:
    def __init__(self, breed, running_speed, coat):
        self.breed = breed
        self.running_speed = running_speed
        self.coat = coat

    def horse_start_stop(self):
        print(str.format("The {0} door is open", self.coat))

    @property
    def breed(self):
        return self.breed

    @breed.setter
    def breed(self, bre):
        self.breed = bre

    @property
    def running_speed(self):
        return self.running_speed

    @running_speed.setter
    def running_speed(self, run):
        self.running_speed = run

    @property
    def coat_type(self):
        return self.coat_type

    @coat_type.setter
    def coat_type(self, coat):
        self.coat_type = coat

my_horse = Horse("scottish", 100, "black")
print(my_horse.coat)
print(my_horse.horse_start_stop)

class Arab(Horse):
    def __init__(self, neck, tail):
        self.neck = neck
        self.tail = tail

    @property
    def neck(self):
        return self.neck
    @neck.setter
    def neck(self, nekk):
        self.neck = nekk

    @property
    def tail(self):
        return self.tail
    @tail.setter
    def neck(self, tall):
        self.tail = tall