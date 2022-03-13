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
