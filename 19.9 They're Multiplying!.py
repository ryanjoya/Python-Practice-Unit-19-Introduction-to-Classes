class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print self.name
        print self.age
        print self.health
hippo = Animal("Harry", 3)
sloth = Animal("Barry", 4)
ocelot = Animal("Larry", 5)
hippo.description()
sloth.description()
ocelot.description()
