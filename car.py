class Car:

    def __init__(self, name="General", model="GM", make=None):
        self.name = name
        self.model = model
        self.make = make
        self.speed = 0

        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.make == "trailer":
            self.num_of_wheels = 8

        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.make != "trailer":
            self.make = "Saloon"
            return True
        else:
            self.make = "trailer"
            return False

    def drive(self, name):

        if self.make == "trailer":
            self.speed = 77
        elif self.name == "Mercedes":
            self.speed = 1000

        return self
