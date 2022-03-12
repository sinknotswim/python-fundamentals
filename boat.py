class Boat:
    def __init__(self, paint_color, max_speed, seats_number):
        self.paint_color = paint_color
        self.max_speed = max_speed
        self.seats_number = seats_number

    def boat_start_stop(self):
        print(str.format("The {0} door is open", self.seats_number))

    def get_paint_color(self):
        return self.paint_color

    def set_paint_color(self, bre):
        self.paint_color = bre

    def get_max_speed(self):
        return self.max_speed

    def set_max_speed(self, run):
        self.max_speed = run

    def get_seats(self):
        return self.seats

    def set_seats(self, seats_number):
        self.seats = seats_number

my_boat = Boat("blue", 100, 10)
print(my_boat.seats_number)
print(my_boat.boat_start_stop)