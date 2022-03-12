class Guitar:
    def __init__(self, number_strings, wood_type, branding):
        self.number_strings = number_strings
        self.wood_type = wood_type
        self.branding = branding

    def guitar_start_stop(self):
        print(str.format("The {0} door is open", self.branding))

    @property
    def number_strings(self):
        return self.number_strings

    @number_strings.setter
    def number_strings(self, string):
        self.number_strings = string

    @property
    def wood_type(self):
        return self.wood_type

    @wood_type.setter
    def wood_type(self, wood):
        self.wood_type = wood

    @property
    def brand(self):
        return self.brand

    @brand.setter
    def brand(self, branding):
        self.brand = branding

my_guitar = Guitar(7, "mahogony", "gibson")
print(my_guitar.branding)
print(my_guitar.guitar_start_stop)