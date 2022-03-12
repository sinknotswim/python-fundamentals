
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