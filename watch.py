class Watch:
    def __init__(self, branding, age, materials):
        self.branding = branding
        self.age = age
        self.materials = materials

    def watch_start_stop(self):
        print(str.format("The {0} door is open", self.materials))

    def get_branding(self):
        return self.branding

    def set_branding(self, bre):
        self.branding = bre

    def get_age(self):
        return self.age

    def set_age(self, run):
        self.age = run

    def get_madeof(self):
        return self.madeof

    def set_madeof(self, materials):
        self.madeof = materials

my_watch = Watch("blue", 100, 10)
print(my_watch.materials)
print(my_watch.watch_start_stop)