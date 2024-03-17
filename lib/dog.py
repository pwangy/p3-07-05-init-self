#!/usr/bin/env python3

class Dog:
    
    def __init__(self, name, breed="Mutt", favorite_toy="Any"):
        self.name = name
        self.favorite_toy = favorite_toy
        self.breed = breed
        # print(f"{name} who is a {breed} has been born!")

    def bark(self):
        print(f"Woof!")

    def showing_self(self):
        return self

    def get_adopted(self, owner_name):
        self.owner = owner_name


fido = Dog("Fido", "Dalmantion")

snoopy = Dog("Snoopy", "Beagle")
snoopy.showing_self()
snoopy is snoopy.showing_self()
snoopy.get_adopted("Chloe")
snoopy.owner