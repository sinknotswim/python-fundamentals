#1 8-3
def make_shirt(size, message):
    print("The shirt is " + size + " and will say " + message + ".")

make_shirt("Large", "I Love Python")
make_shirt(size = "Large", message = "I Love Python")

#8-4

def make_shirt2(size='Large', message='I Love Python'):
    print("The shirt is " + size + " and will say " + message + ".")

make_shirt2(size='Medium')

#8-5

def describe_city(city, country='United States of America'):
    print(city + " is in " + country)

describe_city("Wichita")
describe_city("Detroit")
describe_city("Stockholm", "Sweden")

#2 8-9 to 8-11

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians = ["siegfried & roy", "shin lim", "mitch magic"]

show_magicians(magicians)

#8-10

greats = []

def make_great(magicians):
    while magicians:
        magician = magicians.pop()
        great = magician + " the Great"
        greats.append(great)
    for great in greats:
        print(great.title())

make_great(magicians)
show_magicians(magicians)

#8-11

magicians_copy = ["siegfried & roy", "shin lim", "mitch magic"]
greats = []

def make_great(magicians_copy):
    while magicians_copy:
        magician_copy = magicians_copy.pop()
        great = magician_copy + " the Great"
        greats.append(great)
    for great in greats:
        magicians.append(greats)
        print(great.title())
    return magicians

make_great(magicians_copy)
show_magicians(magicians_copy)

#3 9-1

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name + " serves the best " + self.cuisine_type + ".")
    def open_restaurant(self):
        print(self.restaurant_name + " is open!")

restaurant = Restaurant("Talianos", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2

talianos = Restaurant("Talianos", "Italian")
talianos.describe_restaurant()

olive_garden = Restaurant("Olive Garden", "Italian")
olive_garden.describe_restaurant()

abuelos = Restaurant("Abuelos", "Mexican")
abuelos.describe_restaurant()

#9-3

class User():
    def __init__(self, first_name, last_name, username, number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.number = number
    def describe_user(self):
        print("User: " + self.first_name + self.last_name)
        print("Username: " + self.username + self.number)
    def welcome_user(self):
        print("Welcome " + self.username + "!")

li = User("Li ", "Taylor ", "sinknotswim", "#1720")
li.describe_user()
li.welcome_user

kyle = User("Kyle ", "Cassity ", "Kyntronos", "#1549")
kyle.describe_user()
kyle.welcome_user

michael = User("Michael ", "Bisges ", "Claymore Roomba", "#1230")
michael.describe_user()
michael.welcome_user

#9-4

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name + " serves the best " + self.cuisine_type + ".")
    def open_restaurant(self):
        print(self.restaurant_name + " is open!")
    def set_number_served(self, number_served):
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant('Talianos', 'Italian')
restaurant.describe_restaurant()
print("Customers Served: " + str(restaurant.number_served))
restaurant.number_served = 20
print("Customers Served: " + str(restaurant.number_served))
restaurant.set_number_served(22)
print("Customers Served: " + str(restaurant.number_served))
restaurant.increment_number_served(200)
print("Customers Served: " + str(restaurant.number_served))

#9-5

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

li = User("Li ", "Taylor ", "sinknotswim", "#1720")
li.describe_user()
li.welcome_user

print("Making (2) login attempts: ")
li.increment_login_attempts()
li.increment_login_attempts()
print("Login attempts: " + str(li.login_attempts))

print("Resetting, please wait.")
li.reset_login_attempts()
print("Login attempts: " + str(li.login_attempts))

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



#9-9

class Car():
 def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
 def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()
 def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")
 def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")
 def increment_odometer(self, miles):
    self.odometer_reading += miles
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size == 70:
            print("Upgrading battery now to 85kwh...")
            self.battery_size == 85
        else:
            print("No upgrades avalible.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()